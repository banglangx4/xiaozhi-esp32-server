import os
import shutil
import git
from groq import Groq
from typing import List

# ====================================================================
# A. THIẾT LẬP CẤU HÌNH CỦA AGENT
# ====================================================================
# Đọc API Key Groq từ GitHub Secrets (biến môi trường)
GROQ_API_KEY = os.environ.get("GROQ_API_KEY") 

# Đọc URL Repository từ GitHub Actions (biến môi trường)
REPO_URL = os.environ.get("REPO_URL") 

# Tên mô hình Groq (32K Context)
MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct" 

# Cấu hình nội bộ
TEMP_DIR = "./temp_groq_repo"
OUTPUT_DOC_FILE = "PROJECT_DOCUMENTATION.md"
MAX_CONTEXT_TOKEN = 32000 

# Danh sách THƯ MỤC/TỆP CẦN LOẠI TRỪ để giảm thiểu Token Input
EXCLUDE_DIRS = [
    'node_modules',       # Thư viện JavaScript (RẤT LỚN)
    'vendor',             # Thư viện PHP/Ruby (Lớn)
    'build',              # File đã biên dịch/Build
    'dist',               # File phân phối
    'assets',             # Tài nguyên tĩnh (Ảnh, fonts)
    'images',             # Thư mục ảnh
    'media',              # Tệp media/uploads
    'logs',               # Tệp log
    'data',               # Tệp dữ liệu lớn/thô
    'docs',               # Thư mục tài liệu (Tránh tự phân tích tài liệu cũ)
    '.git', 
    '__pycache__', 
    'venv', 
    'test',               # Thư mục chứa Unit/Integration Tests (Tùy chọn)
    'tests',
    OUTPUT_DOC_FILE       # Loại trừ file kết quả để không tự phân tích chính nó
]
# ====================================================================

# Prompt chuyên gia (Đảm bảo đầu ra chuyên nghiệp)
SYSTEM_PROMPT = """
Bạn là một Kiến trúc sư Phần mềm (Senior Software Architect) và Chuyên gia Tài liệu hóa. 
Nhiệm vụ của bạn là phân tích mã nguồn được cung cấp một cách toàn diện và tự động.
Phản hồi phải tuân thủ nghiêm ngặt cấu trúc sau và sử dụng Markdown chuyên nghiệp:

# DỰ ÁN KỸ THUẬT - PHÂN TÍCH TỰ ĐỘNG BẰNG GROQ
---
## 1. KIẾN TRÚC VÀ CẤU TRÚC DỰ ÁN
Tóm tắt mục đích dự án, ngôn ngữ chính, và kiến trúc (ví dụ: REST API, Frontend SPA, v.v.).

## 2. PHÂN TÍCH MODULE VÀ MỐI QUAN HỆ
Giải thích vai trò của từng file/thư mục chính và mối quan hệ giữa chúng.

## 3. LUỒNG DỮ LIỆU CHÍNH (KEY FLOW)
Mô tả luồng thực thi chính (ví dụ: Yêu cầu người dùng -> API Route -> Controller -> Service -> Database).

## 4. HƯỚNG DẪN TRIỂN KHAI THỰC TẾ
Cung cấp các bước rõ ràng (sử dụng lệnh Terminal) để thiết lập môi trường và chạy dự án.

## 5. GỠ LỖI, RỦI RO & BẢO MẬT
Đề xuất 3-5 điểm yếu tiềm ẩn (lỗi logic, vấn đề bảo mật, hoặc hiệu năng) và cách khắc phục.
---
"""

USER_REQUEST = "Bắt đầu quá trình phân tích code và tạo tài liệu kỹ thuật chi tiết theo định dạng yêu cầu. Code đã được đính kèm."

def estimate_tokens(text: str) -> int:
    """Ước tính số token (thường 1 token ~ 4 ký tự)."""
    return len(text) // 4 + 1

def clone_and_bundle_repo() -> str:
    """Clone repository và gộp các file code thành một chuỗi có cấu trúc."""
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    
    print(f"Đang clone repository từ {REPO_URL}...")
    try:
        git.Repo.clone_from(REPO_URL, TEMP_DIR)
    except git.exc.GitCommandError as e:
        print(f"\n❌ LỖI CLONE GIT: Vui lòng kiểm tra lại URL hoặc Token truy cập. Chi tiết: {e}")
        return ""
    
    code_bundle: List[str] = []
    
    for root, dirs, files in os.walk(TEMP_DIR, topdown=True):
        # Loại trừ các thư mục đã định nghĩa
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]
        
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, TEMP_DIR)
            
            # Kiểm tra loại trừ file (ví dụ: file log lớn)
            if any(relative_path.endswith(ext) for ext in ('.log', '.bin', '.sqlite')):
                 continue

            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    # Cấu trúc hóa file code
                    code_bundle.append(f"\n\n### --- FILE START: {relative_path} ---\n")
                    code_bundle.append(content)
                    code_bundle.append(f"\n### --- FILE END: {relative_path} ---\n")
            except Exception as e:
                # Bỏ qua các file không thể đọc (ví dụ: file binary)
                continue

    # Xóa thư mục tạm sau khi gộp thành công
    shutil.rmtree(TEMP_DIR) 
    print(f"\n✅ Hoàn tất thu thập. Đã xóa thư mục tạm {TEMP_DIR}.")
    
    return "".join(code_bundle)

def analyze_with_groq(code_bundle: str):
    """Gửi code và prompt tới Groq API để phân tích."""
    if not code_bundle:
        return "Quá trình phân tích bị hủy do không thể thu thập code."
    if not GROQ_API_KEY:
        return "❌ LỖI: API Key Groq chưa được thiết lập trong biến môi trường GROQ_API_KEY."

    full_user_prompt = f"{USER_REQUEST}\n\n### MÃ NGUỒN TỔNG HỢP ĐỂ PHÂN TÍCH:\n{code_bundle}"
    
    total_input_text = SYSTEM_PROMPT + full_user_prompt
    request_tokens = estimate_tokens(total_input_text)
    
    print(f"Token Input Ước tính: {request_tokens} / {MAX_CONTEXT_TOKEN}")

    if request_tokens > MAX_CONTEXT_TOKEN:
        return f"\n❌ LỖI LỚN: Tổng số Token ({request_tokens}) vượt quá giới hạn Context ({MAX_CONTEXT_TOKEN}) của mô hình. Vui lòng giảm kích thước dự án hoặc chọn mô hình lớn hơn."
    
    print("Đang gửi yêu cầu phân tích tới Groq API...")
    
    client = Groq(api_key=GROQ_API_KEY)

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": full_user_prompt},
            ],
            model=MODEL_NAME,
            temperature=0.2, 
        )

        return chat_completion.choices[0].message.content
        
    except Exception as e:
        return f"\n❌ LỖI GROQ API: {e}. Vui lòng kiểm tra API Key và giới hạn rate limit."

def run_agent():
    """Thực thi toàn bộ quy trình."""
    print("--- KHỞI CHẠY GROQ DOCUMENTATION AGENT ---")
    
    # 1. Thu thập Code
    code_bundle = clone_and_bundle_repo()
    
    # 2. Phân tích
    analysis_result = analyze_with_groq(code_bundle)
    
    # 3. Lưu kết quả
    if analysis_result.startswith("❌ LỖI") or analysis_result.startswith("Quá trình phân tích bị hủy"):
        print("\n" + analysis_result)
        return

    # Ghi đè lên file cũ
    with open(OUTPUT_DOC_FILE, 'w', encoding='utf-8') as f:
        f.write(analysis_result)
    
    print(f"\n✅ THÀNH CÔNG: Tài liệu đã được tạo và lưu tại: {OUTPUT_DOC_FILE}")

if __name__ == "__main__":
    run_agent()