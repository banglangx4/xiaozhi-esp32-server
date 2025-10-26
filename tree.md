.
├── Dockerfile-server
├── Dockerfile-server-base
├── Dockerfile-web
├── LICENSE
├── README.md
├── README_en.md
├── docker-setup.sh
├── docs
│   ├── Deployment.md
│   ├── Deployment_all.md
│   ├── FAQ.md
│   ├── ali-sms-integration.md
│   ├── contributor_open_letter.md
│   ├── dev-ops-integration.md
│   ├── docker
│   │   ├── nginx.conf
│   │   └── start.sh
│   ├── docker-build.md
│   ├── firmware-build.md
│   ├── firmware-setting.md
│   ├── fish-speech-integration.md
│   ├── homeassistant-integration.md
│   ├── huoshan-streamTTS-voice-cloning.md
│   ├── images
│   │   ├── __init__.py
│   │   ├── alisms
│   │   │   ├── sms-01.png
│   │   │   ├── sms-02.png
│   │   │   ├── sms-11.png
│   │   │   ├── sms-21.png
│   │   │   ├── sms-22.png
│   │   │   ├── sms-23.png
│   │   │   ├── sms-24.png
│   │   │   ├── sms-25.png
│   │   │   ├── sms-31.png
│   │   │   └── sms-32.png
│   │   ├── banner1.png
│   │   ├── banner2.png
│   │   ├── conda_env_1.png
│   │   ├── conda_env_2.png
│   │   ├── demo0.png
│   │   ├── demo1.png
│   │   ├── demo10.png
│   │   ├── demo11.png
│   │   ├── demo12.png
│   │   ├── demo13.png
│   │   ├── demo14.png
│   │   ├── demo2.png
│   │   ├── demo3.png
│   │   ├── demo4.png
│   │   ├── demo5.png
│   │   ├── demo6.png
│   │   ├── demo7.png
│   │   ├── demo8.png
│   │   ├── demo9.png
│   │   ├── deploy1.png
│   │   ├── deploy2.png
│   │   ├── firmware-setting-ota.png
│   │   ├── fishspeech
│   │   │   ├── autodl-01.png
│   │   │   └── autodl-02.png
│   │   ├── hnlg.jpg
│   │   ├── image-clone-integration-01.png
│   │   ├── image-clone-integration-02.png
│   │   ├── image-clone-integration-03.png
│   │   ├── image-ha-integration-01.png
│   │   ├── image-ha-integration-02.png
│   │   ├── image-ha-integration-03.png
│   │   ├── image-ha-integration-04.png
│   │   ├── image-ha-integration-05.png
│   │   ├── image-ha-integration-06.png
│   │   ├── logo_bailing.png
│   │   ├── logo_contributors.png
│   │   ├── logo_huiyuan.png
│   │   ├── logo_junsen.png
│   │   ├── logo_qinren.png
│   │   ├── logo_tenclass.png
│   │   ├── logo_xuanfeng.png
│   │   └── manager-mobile
│   │       ├── 打包发行步骤1.png
│   │       ├── 打包发行步骤2.png
│   │       ├── 本地运行.png
│   │       ├── 生成appid.png
│   │       └── 重新识别项目.png
│   ├── index-stream-integration.md
│   ├── mcp-endpoint-enable.md
│   ├── mcp-endpoint-integration.md
│   ├── mcp-vision-integration.md
│   ├── mqtt-gateway-integration.md
│   ├── newsnow_plugin_config.md
│   ├── paddlespeech-deploy.md
│   ├── performance_tester.md
│   ├── voiceprint-integration.md
│   └── weather-integration.md
├── main
│   ├── README.md
│   ├── README_en.md
│   ├── manager-api
│   │   ├── README.md
│   │   ├── pom.xml
│   │   └── src
│   │       ├── main
│   │       │   ├── java
│   │       │   │   └── xiaozhi
│   │       │   │       ├── AdminApplication.java
│   │       │   │       ├── common
│   │       │   │       │   ├── annotation
│   │       │   │       │   │   ├── DataFilter.java
│   │       │   │       │   │   └── LogOperation.java
│   │       │   │       │   ├── aspect
│   │       │   │       │   │   └── RedisAspect.java
│   │       │   │       │   ├── config
│   │       │   │       │   │   ├── AsyncConfig.java
│   │       │   │       │   │   ├── MybatisPlusConfig.java
│   │       │   │       │   │   ├── RestTemplateConfig.java
│   │       │   │       │   │   └── SwaggerConfig.java
│   │       │   │       │   ├── constant
│   │       │   │       │   │   └── Constant.java
│   │       │   │       │   ├── convert
│   │       │   │       │   │   └── DateConverter.java
│   │       │   │       │   ├── dao
│   │       │   │       │   │   └── BaseDao.java
│   │       │   │       │   ├── entity
│   │       │   │       │   │   └── BaseEntity.java
│   │       │   │       │   ├── exception
│   │       │   │       │   │   ├── ErrorCode.java
│   │       │   │       │   │   ├── RenException.java
│   │       │   │       │   │   └── RenExceptionHandler.java
│   │       │   │       │   ├── handler
│   │       │   │       │   │   └── FieldMetaObjectHandler.java
│   │       │   │       │   ├── interceptor
│   │       │   │       │   │   ├── DataFilterInterceptor.java
│   │       │   │       │   │   └── DataScope.java
│   │       │   │       │   ├── page
│   │       │   │       │   │   ├── PageData.java
│   │       │   │       │   │   └── TokenDTO.java
│   │       │   │       │   ├── redis
│   │       │   │       │   │   ├── RedisConfig.java
│   │       │   │       │   │   ├── RedisKeys.java
│   │       │   │       │   │   └── RedisUtils.java
│   │       │   │       │   ├── service
│   │       │   │       │   │   ├── BaseService.java
│   │       │   │       │   │   ├── CrudService.java
│   │       │   │       │   │   └── impl
│   │       │   │       │   │       ├── BaseServiceImpl.java
│   │       │   │       │   │       └── CrudServiceImpl.java
│   │       │   │       │   ├── user
│   │       │   │       │   │   └── UserDetail.java
│   │       │   │       │   ├── utils
│   │       │   │       │   │   ├── AESUtils.java
│   │       │   │       │   │   ├── ConvertUtils.java
│   │       │   │       │   │   ├── DateUtils.java
│   │       │   │       │   │   ├── HashEncryptionUtil.java
│   │       │   │       │   │   ├── HttpContextUtils.java
│   │       │   │       │   │   ├── IpUtils.java
│   │       │   │       │   │   ├── JsonRpcTwo.java
│   │       │   │       │   │   ├── JsonUtils.java
│   │       │   │       │   │   ├── MessageUtils.java
│   │       │   │       │   │   ├── PropertiesUtils.java
│   │       │   │       │   │   ├── ResourcesUtils.java
│   │       │   │       │   │   ├── Result.java
│   │       │   │       │   │   ├── ResultUtils.java
│   │       │   │       │   │   ├── SM2Utils.java
│   │       │   │       │   │   ├── SensitiveDataUtils.java
│   │       │   │       │   │   ├── Sm2DecryptUtil.java
│   │       │   │       │   │   ├── SpringContextUtils.java
│   │       │   │       │   │   ├── TreeNode.java
│   │       │   │       │   │   └── TreeUtils.java
│   │       │   │       │   ├── validator
│   │       │   │       │   │   ├── AssertUtils.java
│   │       │   │       │   │   ├── ValidatorUtils.java
│   │       │   │       │   │   └── group
│   │       │   │       │   │       ├── AddGroup.java
│   │       │   │       │   │       ├── DefaultGroup.java
│   │       │   │       │   │       └── UpdateGroup.java
│   │       │   │       │   └── xss
│   │       │   │       │       ├── SqlFilter.java
│   │       │   │       │       ├── XssConfig.java
│   │       │   │       │       ├── XssFilter.java
│   │       │   │       │       ├── XssHttpServletRequestWrapper.java
│   │       │   │       │       ├── XssProperties.java
│   │       │   │       │       └── XssUtils.java
│   │       │   │       └── modules
│   │       │   │           ├── agent
│   │       │   │           │   ├── Enums
│   │       │   │           │   │   ├── AgentChatHistoryType.java
│   │       │   │           │   │   └── XiaoZhiMcpJsonRpcJson.java
│   │       │   │           │   ├── controller
│   │       │   │           │   │   ├── AgentChatHistoryController.java
│   │       │   │           │   │   ├── AgentController.java
│   │       │   │           │   │   ├── AgentMcpAccessPointController.java
│   │       │   │           │   │   ├── AgentTemplateController.java
│   │       │   │           │   │   └── AgentVoicePrintController.java
│   │       │   │           │   ├── dao
│   │       │   │           │   │   ├── AgentDao.java
│   │       │   │           │   │   ├── AgentPluginMappingMapper.java
│   │       │   │           │   │   ├── AgentTemplateDao.java
│   │       │   │           │   │   ├── AgentVoicePrintDao.java
│   │       │   │           │   │   ├── AiAgentChatAudioDao.java
│   │       │   │           │   │   └── AiAgentChatHistoryDao.java
│   │       │   │           │   ├── dto
│   │       │   │           │   │   ├── AgentChatHistoryDTO.java
│   │       │   │           │   │   ├── AgentChatHistoryReportDTO.java
│   │       │   │           │   │   ├── AgentChatSessionDTO.java
│   │       │   │           │   │   ├── AgentCreateDTO.java
│   │       │   │           │   │   ├── AgentDTO.java
│   │       │   │           │   │   ├── AgentMemoryDTO.java
│   │       │   │           │   │   ├── AgentUpdateDTO.java
│   │       │   │           │   │   ├── AgentVoicePrintSaveDTO.java
│   │       │   │           │   │   ├── AgentVoicePrintUpdateDTO.java
│   │       │   │           │   │   ├── IdentifyVoicePrintResponse.java
│   │       │   │           │   │   └── McpJsonRpcResponse.java
│   │       │   │           │   ├── entity
│   │       │   │           │   │   ├── AgentChatAudioEntity.java
│   │       │   │           │   │   ├── AgentChatHistoryEntity.java
│   │       │   │           │   │   ├── AgentEntity.java
│   │       │   │           │   │   ├── AgentPluginMapping.java
│   │       │   │           │   │   ├── AgentTemplateEntity.java
│   │       │   │           │   │   └── AgentVoicePrintEntity.java
│   │       │   │           │   ├── service
│   │       │   │           │   │   ├── AgentChatAudioService.java
│   │       │   │           │   │   ├── AgentChatHistoryService.java
│   │       │   │           │   │   ├── AgentMcpAccessPointService.java
│   │       │   │           │   │   ├── AgentPluginMappingService.java
│   │       │   │           │   │   ├── AgentService.java
│   │       │   │           │   │   ├── AgentTemplateService.java
│   │       │   │           │   │   ├── AgentVoicePrintService.java
│   │       │   │           │   │   ├── biz
│   │       │   │           │   │   │   ├── AgentChatHistoryBizService.java
│   │       │   │           │   │   │   └── impl
│   │       │   │           │   │   │       └── AgentChatHistoryBizServiceImpl.java
│   │       │   │           │   │   └── impl
│   │       │   │           │   │       ├── AgentChatAudioServiceImpl.java
│   │       │   │           │   │       ├── AgentChatHistoryServiceImpl.java
│   │       │   │           │   │       ├── AgentMcpAccessPointServiceImpl.java
│   │       │   │           │   │       ├── AgentPluginMappingServiceImpl.java
│   │       │   │           │   │       ├── AgentServiceImpl.java
│   │       │   │           │   │       ├── AgentTemplateServiceImpl.java
│   │       │   │           │   │       └── AgentVoicePrintServiceImpl.java
│   │       │   │           │   └── vo
│   │       │   │           │       ├── AgentChatHistoryUserVO.java
│   │       │   │           │       ├── AgentInfoVO.java
│   │       │   │           │       ├── AgentTemplateVO.java
│   │       │   │           │       └── AgentVoicePrintVO.java
│   │       │   │           ├── config
│   │       │   │           │   ├── controller
│   │       │   │           │   │   └── ConfigController.java
│   │       │   │           │   ├── dto
│   │       │   │           │   │   └── AgentModelsDTO.java
│   │       │   │           │   ├── init
│   │       │   │           │   │   └── SystemInitConfig.java
│   │       │   │           │   └── service
│   │       │   │           │       ├── ConfigService.java
│   │       │   │           │       └── impl
│   │       │   │           │           └── ConfigServiceImpl.java
│   │       │   │           ├── device
│   │       │   │           │   ├── controller
│   │       │   │           │   │   ├── DeviceController.java
│   │       │   │           │   │   ├── OTAController.java
│   │       │   │           │   │   └── OTAMagController.java
│   │       │   │           │   ├── dao
│   │       │   │           │   │   ├── DeviceDao.java
│   │       │   │           │   │   └── OtaDao.java
│   │       │   │           │   ├── dto
│   │       │   │           │   │   ├── DeviceBindDTO.java
│   │       │   │           │   │   ├── DeviceManualAddDTO.java
│   │       │   │           │   │   ├── DevicePageUserDTO.java
│   │       │   │           │   │   ├── DeviceRegisterDTO.java
│   │       │   │           │   │   ├── DeviceReportReqDTO.java
│   │       │   │           │   │   ├── DeviceReportRespDTO.java
│   │       │   │           │   │   ├── DeviceUnBindDTO.java
│   │       │   │           │   │   └── DeviceUpdateDTO.java
│   │       │   │           │   ├── entity
│   │       │   │           │   │   ├── DeviceEntity.java
│   │       │   │           │   │   └── OtaEntity.java
│   │       │   │           │   ├── service
│   │       │   │           │   │   ├── DeviceService.java
│   │       │   │           │   │   ├── OtaService.java
│   │       │   │           │   │   └── impl
│   │       │   │           │   │       ├── DeviceServiceImpl.java
│   │       │   │           │   │       └── OtaServiceImpl.java
│   │       │   │           │   └── vo
│   │       │   │           │       ├── DeviceOtaVO.java
│   │       │   │           │       └── UserShowDeviceListVO.java
│   │       │   │           ├── model
│   │       │   │           │   ├── controller
│   │       │   │           │   │   ├── ModelController.java
│   │       │   │           │   │   └── ModelProviderController.java
│   │       │   │           │   ├── dao
│   │       │   │           │   │   ├── ModelConfigDao.java
│   │       │   │           │   │   └── ModelProviderDao.java
│   │       │   │           │   ├── dto
│   │       │   │           │   │   ├── LlmModelBasicInfoDTO.java
│   │       │   │           │   │   ├── ModelBasicInfoDTO.java
│   │       │   │           │   │   ├── ModelConfigBodyDTO.java
│   │       │   │           │   │   ├── ModelConfigDTO.java
│   │       │   │           │   │   ├── ModelProviderDTO.java
│   │       │   │           │   │   └── VoiceDTO.java
│   │       │   │           │   ├── entity
│   │       │   │           │   │   ├── ModelConfigEntity.java
│   │       │   │           │   │   └── ModelProviderEntity.java
│   │       │   │           │   └── service
│   │       │   │           │       ├── ModelConfigService.java
│   │       │   │           │       ├── ModelProviderService.java
│   │       │   │           │       └── impl
│   │       │   │           │           ├── ModelConfigServiceImpl.java
│   │       │   │           │           └── ModelProviderServiceImpl.java
│   │       │   │           ├── security
│   │       │   │           │   ├── config
│   │       │   │           │   │   ├── FilterConfig.java
│   │       │   │           │   │   ├── ShiroConfig.java
│   │       │   │           │   │   └── WebMvcConfig.java
│   │       │   │           │   ├── controller
│   │       │   │           │   │   └── LoginController.java
│   │       │   │           │   ├── dao
│   │       │   │           │   │   └── SysUserTokenDao.java
│   │       │   │           │   ├── dto
│   │       │   │           │   │   ├── LoginDTO.java
│   │       │   │           │   │   └── SmsVerificationDTO.java
│   │       │   │           │   ├── entity
│   │       │   │           │   │   └── SysUserTokenEntity.java
│   │       │   │           │   ├── oauth2
│   │       │   │           │   │   ├── Oauth2Filter.java
│   │       │   │           │   │   ├── Oauth2Realm.java
│   │       │   │           │   │   ├── Oauth2Token.java
│   │       │   │           │   │   └── TokenGenerator.java
│   │       │   │           │   ├── password
│   │       │   │           │   │   ├── BCrypt.java
│   │       │   │           │   │   ├── BCryptPasswordEncoder.java
│   │       │   │           │   │   ├── PasswordEncoder.java
│   │       │   │           │   │   └── PasswordUtils.java
│   │       │   │           │   ├── secret
│   │       │   │           │   │   ├── ServerSecretFilter.java
│   │       │   │           │   │   └── ServerSecretToken.java
│   │       │   │           │   ├── service
│   │       │   │           │   │   ├── CaptchaService.java
│   │       │   │           │   │   ├── ShiroService.java
│   │       │   │           │   │   ├── SysUserTokenService.java
│   │       │   │           │   │   └── impl
│   │       │   │           │   │       ├── CaptchaServiceImpl.java
│   │       │   │           │   │       ├── ShiroServiceImpl.java
│   │       │   │           │   │       └── SysUserTokenServiceImpl.java
│   │       │   │           │   └── user
│   │       │   │           │       └── SecurityUser.java
│   │       │   │           ├── sms
│   │       │   │           │   └── service
│   │       │   │           │       ├── SmsService.java
│   │       │   │           │       └── imp
│   │       │   │           │           └── ALiYunSmsService.java
│   │       │   │           ├── sys
│   │       │   │           │   ├── controller
│   │       │   │           │   │   ├── AdminController.java
│   │       │   │           │   │   ├── ServerSideManageController.java
│   │       │   │           │   │   ├── SysDictDataController.java
│   │       │   │           │   │   ├── SysDictTypeController.java
│   │       │   │           │   │   └── SysParamsController.java
│   │       │   │           │   ├── dao
│   │       │   │           │   │   ├── SysDictDataDao.java
│   │       │   │           │   │   ├── SysDictTypeDao.java
│   │       │   │           │   │   ├── SysParamsDao.java
│   │       │   │           │   │   └── SysUserDao.java
│   │       │   │           │   ├── dto
│   │       │   │           │   │   ├── AdminPageUserDTO.java
│   │       │   │           │   │   ├── EmitSeverActionDTO.java
│   │       │   │           │   │   ├── PasswordDTO.java
│   │       │   │           │   │   ├── RetrievePasswordDTO.java
│   │       │   │           │   │   ├── ServerActionPayloadDTO.java
│   │       │   │           │   │   ├── ServerActionResponseDTO.java
│   │       │   │           │   │   ├── SysDictDataDTO.java
│   │       │   │           │   │   ├── SysDictTypeDTO.java
│   │       │   │           │   │   ├── SysParamsDTO.java
│   │       │   │           │   │   └── SysUserDTO.java
│   │       │   │           │   ├── entity
│   │       │   │           │   │   ├── SysDictDataEntity.java
│   │       │   │           │   │   ├── SysDictTypeEntity.java
│   │       │   │           │   │   ├── SysParamsEntity.java
│   │       │   │           │   │   └── SysUserEntity.java
│   │       │   │           │   ├── enums
│   │       │   │           │   │   ├── ServerActionEnum.java
│   │       │   │           │   │   ├── ServerActionResponseEnum.java
│   │       │   │           │   │   └── SuperAdminEnum.java
│   │       │   │           │   ├── redis
│   │       │   │           │   │   └── SysParamsRedis.java
│   │       │   │           │   ├── service
│   │       │   │           │   │   ├── SysDictDataService.java
│   │       │   │           │   │   ├── SysDictTypeService.java
│   │       │   │           │   │   ├── SysParamsService.java
│   │       │   │           │   │   ├── SysUserService.java
│   │       │   │           │   │   ├── SysUserUtilService.java
│   │       │   │           │   │   ├── TokenService.java
│   │       │   │           │   │   └── impl
│   │       │   │           │   │       ├── SysDictDataServiceImpl.java
│   │       │   │           │   │       ├── SysDictTypeServiceImpl.java
│   │       │   │           │   │       ├── SysParamsServiceImpl.java
│   │       │   │           │   │       ├── SysUserServiceImpl.java
│   │       │   │           │   │       ├── SysUserUtilServiceImpl.java
│   │       │   │           │   │       └── TokenServiceImpl.java
│   │       │   │           │   ├── utils
│   │       │   │           │   │   ├── WebSocketClientManager.java
│   │       │   │           │   │   ├── WebSocketTestHandler.java
│   │       │   │           │   │   └── WebSocketValidator.java
│   │       │   │           │   └── vo
│   │       │   │           │       ├── AdminPageUserVO.java
│   │       │   │           │       ├── SysDictDataItem.java
│   │       │   │           │       ├── SysDictDataVO.java
│   │       │   │           │       └── SysDictTypeVO.java
│   │       │   │           ├── timbre
│   │       │   │           │   ├── controller
│   │       │   │           │   │   └── TimbreController.java
│   │       │   │           │   ├── dao
│   │       │   │           │   │   └── TimbreDao.java
│   │       │   │           │   ├── dto
│   │       │   │           │   │   ├── TimbreDataDTO.java
│   │       │   │           │   │   └── TimbrePageDTO.java
│   │       │   │           │   ├── entity
│   │       │   │           │   │   └── TimbreEntity.java
│   │       │   │           │   ├── service
│   │       │   │           │   │   ├── TimbreService.java
│   │       │   │           │   │   └── impl
│   │       │   │           │   │       └── TimbreServiceImpl.java
│   │       │   │           │   └── vo
│   │       │   │           │       └── TimbreDetailsVO.java
│   │       │   │           └── voiceclone
│   │       │   │               ├── controller
│   │       │   │               │   ├── VoiceCloneController.java
│   │       │   │               │   └── VoiceResourceController.java
│   │       │   │               ├── dao
│   │       │   │               │   └── VoiceCloneDao.java
│   │       │   │               ├── dto
│   │       │   │               │   ├── VoiceCloneDTO.java
│   │       │   │               │   └── VoiceCloneResponseDTO.java
│   │       │   │               ├── entity
│   │       │   │               │   └── VoiceCloneEntity.java
│   │       │   │               └── service
│   │       │   │                   ├── VoiceCloneService.java
│   │       │   │                   └── impl
│   │       │   │                       └── VoiceCloneServiceImpl.java
│   │       │   └── resources
│   │       │       ├── application-dev.yml
│   │       │       ├── application.yml
│   │       │       ├── db
│   │       │       │   └── changelog
│   │       │       │       ├── 202503141335.sql
│   │       │       │       ├── 202503141346.sql
│   │       │       │       ├── 202504082211.sql
│   │       │       │       ├── 202504092335.sql
│   │       │       │       ├── 202504112044.sql
│   │       │       │       ├── 202504112058.sql
│   │       │       │       ├── 202504151206.sql
│   │       │       │       ├── 202504181536.sql
│   │       │       │       ├── 202504221135.sql
│   │       │       │       ├── 202504221555.sql
│   │       │       │       ├── 202504251422.sql
│   │       │       │       ├── 202504291043.sql
│   │       │       │       ├── 202504301341.sql
│   │       │       │       ├── 202505022134.sql
│   │       │       │       ├── 202505081146.sql
│   │       │       │       ├── 202505091555.sql
│   │       │       │       ├── 202505111914.sql
│   │       │       │       ├── 202505122348.sql
│   │       │       │       ├── 202505142037.sql
│   │       │       │       ├── 202505151451.sql
│   │       │       │       ├── 202505182234.sql
│   │       │       │       ├── 202505201744.sql
│   │       │       │       ├── 202505271414.sql
│   │       │       │       ├── 202505292203.sql
│   │       │       │       ├── 202506010920.sql
│   │       │       │       ├── 202506031639.sql
│   │       │       │       ├── 202506032232.sql
│   │       │       │       ├── 202506051538.sql
│   │       │       │       ├── 202506080955.sql
│   │       │       │       ├── 202506091720.sql
│   │       │       │       ├── 202506161101.sql
│   │       │       │       ├── 202506191643.sql
│   │       │       │       ├── 202506251620.sql
│   │       │       │       ├── 202506261637.sql
│   │       │       │       ├── 202507031602.sql
│   │       │       │       ├── 202507041018.sql
│   │       │       │       ├── 202507071130.sql
│   │       │       │       ├── 202507071530.sql
│   │       │       │       ├── 202507081646.sql
│   │       │       │       ├── 202507101203.sql
│   │       │       │       ├── 202508081701.sql
│   │       │       │       ├── 202508111734.sql
│   │       │       │       ├── 202508131557.sql
│   │       │       │       ├── 202508271113.sql
│   │       │       │       ├── 202509051745.sql
│   │       │       │       ├── 202509080922.sql
│   │       │       │       ├── 202509081140.sql
│   │       │       │       ├── 202509091042.sql
│   │       │       │       ├── 202509091633.sql
│   │       │       │       ├── 202509161610.sql
│   │       │       │       ├── 202509161701.sql
│   │       │       │       ├── 202509191545.sql
│   │       │       │       ├── 202509220926.sql
│   │       │       │       ├── 202509220958.sql
│   │       │       │       ├── 202509221530.sql
│   │       │       │       ├── 202510071522.sql
│   │       │       │       ├── 202510191042.sql
│   │       │       │       └── db.changelog-master.yaml
│   │       │       ├── i18n
│   │       │       │   ├── messages.properties
│   │       │       │   ├── messages_en_US.properties
│   │       │       │   ├── messages_zh_CN.properties
│   │       │       │   ├── messages_zh_TW.properties
│   │       │       │   ├── validation.properties
│   │       │       │   ├── validation_en_US.properties
│   │       │       │   ├── validation_zh_CN.properties
│   │       │       │   └── validation_zh_TW.properties
│   │       │       ├── logback-spring.xml
│   │       │       ├── lua
│   │       │       │   ├── emptyAll.lua
│   │       │       │   └── getKeyOrCreate.lua
│   │       │       └── mapper
│   │       │           ├── agent
│   │       │           │   ├── AgentDao.xml
│   │       │           │   ├── AgentPluginMappingMapper.xml
│   │       │           │   ├── AgentTemplateMapper.xml
│   │       │           │   └── AiAgentChatHistoryDao.xml
│   │       │           ├── device
│   │       │           │   └── DeviceDao.xml
│   │       │           ├── model
│   │       │           │   ├── ModelConfigDao.xml
│   │       │           │   └── ModelProviderDao.xml
│   │       │           ├── security
│   │       │           │   └── SysUserTokenDao.xml
│   │       │           ├── sys
│   │       │           │   ├── SysDictDataDao.xml
│   │       │           │   ├── SysDictTypeDao.xml
│   │       │           │   ├── SysParamsDao.xml
│   │       │           │   └── SysUserDao.xml
│   │       │           └── voiceclone
│   │       │               └── VoiceCloneDao.xml
│   │       └── test
│   │           ├── java
│   │           │   └── xiaozhi
│   │           │       ├── common
│   │           │       │   └── utils
│   │           │       │       └── AESUtilsTest.java
│   │           │       └── modules
│   │           │           ├── device
│   │           │           │   └── DeviceTest.java
│   │           │           └── sys
│   │           │               └── loginControllerTest.java
│   │           └── resources
│   │               └── application.yml
│   ├── manager-mobile
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── env
│   │   ├── eslint.config.mjs
│   │   ├── favicon.ico
│   │   ├── index.html
│   │   ├── manifest.config.ts
│   │   ├── package.json
│   │   ├── pages.config.ts
│   │   ├── patches
│   │   │   └── @dcloudio__uni-h5.patch
│   │   ├── pnpm-lock.yaml
│   │   ├── pnpm-workspace.yaml
│   │   ├── scripts
│   │   │   └── postupgrade.js
│   │   ├── src
│   │   │   ├── App.vue
│   │   │   ├── api
│   │   │   │   ├── agent
│   │   │   │   │   ├── agent.ts
│   │   │   │   │   └── types.ts
│   │   │   │   ├── auth.ts
│   │   │   │   ├── chat-history
│   │   │   │   │   ├── chat-history.ts
│   │   │   │   │   ├── index.ts
│   │   │   │   │   └── types.ts
│   │   │   │   ├── device
│   │   │   │   │   ├── device.ts
│   │   │   │   │   ├── index.ts
│   │   │   │   │   └── types.ts
│   │   │   │   └── voiceprint
│   │   │   │       ├── index.ts
│   │   │   │       ├── types.ts
│   │   │   │       └── voiceprint.ts
│   │   │   ├── components
│   │   │   │   └── custom-tabs
│   │   │   │       └── index.vue
│   │   │   ├── env.d.ts
│   │   │   ├── hooks
│   │   │   │   ├── usePageAuth.ts
│   │   │   │   ├── useRequest.ts
│   │   │   │   └── useUpload.ts
│   │   │   ├── http
│   │   │   │   ├── README.md
│   │   │   │   └── request
│   │   │   │       ├── alova.ts
│   │   │   │       ├── enum.ts
│   │   │   │       └── types.ts
│   │   │   ├── i18n
│   │   │   │   ├── en.ts
│   │   │   │   ├── index.ts
│   │   │   │   ├── zh_CN.ts
│   │   │   │   └── zh_TW.ts
│   │   │   ├── layouts
│   │   │   │   ├── default.vue
│   │   │   │   ├── fg-tabbar
│   │   │   │   │   ├── fg-tabbar.vue
│   │   │   │   │   ├── tabbar.md
│   │   │   │   │   ├── tabbar.ts
│   │   │   │   │   └── tabbarList.ts
│   │   │   │   └── tabbar.vue
│   │   │   ├── main.ts
│   │   │   ├── manifest.json
│   │   │   ├── pages
│   │   │   │   ├── agent
│   │   │   │   │   ├── edit.vue
│   │   │   │   │   ├── index.vue
│   │   │   │   │   └── tools.vue
│   │   │   │   ├── chat-history
│   │   │   │   │   ├── detail.vue
│   │   │   │   │   └── index.vue
│   │   │   │   ├── device
│   │   │   │   │   └── index.vue
│   │   │   │   ├── device-config
│   │   │   │   │   ├── components
│   │   │   │   │   │   ├── ultrasonic-config.vue
│   │   │   │   │   │   ├── wifi-config.vue
│   │   │   │   │   │   └── wifi-selector.vue
│   │   │   │   │   └── index.vue
│   │   │   │   ├── forgot-password
│   │   │   │   │   └── index.vue
│   │   │   │   ├── index
│   │   │   │   │   └── index.vue
│   │   │   │   ├── login
│   │   │   │   │   └── index.vue
│   │   │   │   ├── register
│   │   │   │   │   └── index.vue
│   │   │   │   ├── settings
│   │   │   │   │   └── index.vue
│   │   │   │   └── voiceprint
│   │   │   │       └── index.vue
│   │   │   ├── pages-sub
│   │   │   │   └── demo
│   │   │   │       └── index.vue
│   │   │   ├── pages.json
│   │   │   ├── router
│   │   │   │   └── interceptor.ts
│   │   │   ├── static
│   │   │   │   ├── app
│   │   │   │   │   └── icons
│   │   │   │   │       ├── 1024x1024.png
│   │   │   │   │       ├── 120x120.png
│   │   │   │   │       ├── 144x144.png
│   │   │   │   │       ├── 152x152.png
│   │   │   │   │       ├── 167x167.png
│   │   │   │   │       ├── 180x180.png
│   │   │   │   │       ├── 192x192.png
│   │   │   │   │       ├── 20x20.png
│   │   │   │   │       ├── 29x29.png
│   │   │   │   │       ├── 40x40.png
│   │   │   │   │       ├── 58x58.png
│   │   │   │   │       ├── 60x60.png
│   │   │   │   │       ├── 72x72.png
│   │   │   │   │       ├── 76x76.png
│   │   │   │   │       ├── 80x80.png
│   │   │   │   │       ├── 87x87.png
│   │   │   │   │       └── 96x96.png
│   │   │   │   ├── images
│   │   │   │   │   ├── default-avatar.png
│   │   │   │   │   └── home
│   │   │   │   │       └── main-top-bg.png
│   │   │   │   ├── logo.png
│   │   │   │   ├── logo.svg
│   │   │   │   └── tabbar
│   │   │   │       ├── chat.png
│   │   │   │       ├── chat_activate.png
│   │   │   │       ├── device.png
│   │   │   │       ├── device_activate.png
│   │   │   │       ├── example.png
│   │   │   │       ├── exampleHL.png
│   │   │   │       ├── home.png
│   │   │   │       ├── homeHL.png
│   │   │   │       ├── microphone.png
│   │   │   │       ├── microphone_activate.png
│   │   │   │       ├── network.png
│   │   │   │       ├── network_activate.png
│   │   │   │       ├── personal.png
│   │   │   │       ├── personalHL.png
│   │   │   │       ├── robot.png
│   │   │   │       ├── robot_activate.png
│   │   │   │       ├── system.png
│   │   │   │       └── system_activate.png
│   │   │   ├── store
│   │   │   │   ├── config.ts
│   │   │   │   ├── index.ts
│   │   │   │   ├── lang.ts
│   │   │   │   ├── plugin.ts
│   │   │   │   └── user.ts
│   │   │   ├── style
│   │   │   │   ├── iconfont.css
│   │   │   │   └── index.scss
│   │   │   ├── typings.d.ts
│   │   │   ├── typings.ts
│   │   │   ├── uni.scss
│   │   │   └── utils
│   │   │       ├── index.ts
│   │   │       ├── platform.ts
│   │   │       ├── toast.ts
│   │   │       └── uploadFile.ts
│   │   ├── tsconfig.json
│   │   ├── uno.config.ts
│   │   ├── unpackage
│   │   │   └── res
│   │   │       └── icons
│   │   │           ├── 1024x1024.png
│   │   │           ├── 120x120.png
│   │   │           ├── 144x144.png
│   │   │           ├── 152x152.png
│   │   │           ├── 167x167.png
│   │   │           ├── 180x180.png
│   │   │           ├── 192x192.png
│   │   │           ├── 20x20.png
│   │   │           ├── 29x29.png
│   │   │           ├── 40x40.png
│   │   │           ├── 58x58.png
│   │   │           ├── 60x60.png
│   │   │           ├── 72x72.png
│   │   │           ├── 76x76.png
│   │   │           ├── 80x80.png
│   │   │           ├── 87x87.png
│   │   │           └── 96x96.png
│   │   └── vite.config.ts
│   ├── manager-web
│   │   ├── README.md
│   │   ├── babel.config.js
│   │   ├── jsconfig.json
│   │   ├── package-lock.json
│   │   ├── package.json
│   │   ├── public
│   │   │   ├── favicon.ico
│   │   │   ├── index.html
│   │   │   └── offline.html
│   │   ├── src
│   │   │   ├── App.vue
│   │   │   ├── apis
│   │   │   │   ├── api.js
│   │   │   │   ├── httpRequest.js
│   │   │   │   └── module
│   │   │   │       ├── admin.js
│   │   │   │       ├── agent.js
│   │   │   │       ├── device.js
│   │   │   │       ├── dict.js
│   │   │   │       ├── model.js
│   │   │   │       ├── ota.js
│   │   │   │       ├── timbre.js
│   │   │   │       ├── user.js
│   │   │   │       ├── voiceClone.js
│   │   │   │       └── voiceResource.js
│   │   │   ├── assets
│   │   │   │   ├── header
│   │   │   │   │   ├── model_config.png
│   │   │   │   │   ├── param_management.png
│   │   │   │   │   ├── robot.png
│   │   │   │   │   ├── user_management.png
│   │   │   │   │   └── voice.png
│   │   │   │   ├── home
│   │   │   │   │   ├── avatar.png
│   │   │   │   │   ├── close.png
│   │   │   │   │   ├── delete.png
│   │   │   │   │   ├── equipment.png
│   │   │   │   │   ├── info.png
│   │   │   │   │   ├── main-top-bg.png
│   │   │   │   │   ├── red-info.png
│   │   │   │   │   ├── search.png
│   │   │   │   │   └── setting-user.png
│   │   │   │   ├── login
│   │   │   │   │   ├── down-arrow.png
│   │   │   │   │   ├── hi.png
│   │   │   │   │   ├── login-person.png
│   │   │   │   │   ├── password.png
│   │   │   │   │   ├── phone.png
│   │   │   │   │   ├── register-person.png
│   │   │   │   │   ├── shield.png
│   │   │   │   │   └── username.png
│   │   │   │   ├── model
│   │   │   │   │   ├── inner_conf.png
│   │   │   │   │   ├── model.png
│   │   │   │   │   └── output_conf.png
│   │   │   │   ├── user-avatar1.png
│   │   │   │   ├── user-avatar2.png
│   │   │   │   ├── user-avatar3.png
│   │   │   │   ├── user-avatar4.png
│   │   │   │   ├── user-avatar5.png
│   │   │   │   ├── xiaozhi-ai.png
│   │   │   │   └── xiaozhi-logo.png
│   │   │   ├── components
│   │   │   │   ├── AddDeviceDialog.vue
│   │   │   │   ├── AddModelDialog.vue
│   │   │   │   ├── AddWisdomBodyDialog.vue
│   │   │   │   ├── AudioPlayer.vue
│   │   │   │   ├── CacheViewer.vue
│   │   │   │   ├── ChangePasswordDialog.vue
│   │   │   │   ├── ChatHistoryDialog.vue
│   │   │   │   ├── DeviceItem.vue
│   │   │   │   ├── DictDataDialog.vue
│   │   │   │   ├── DictTypeDialog.vue
│   │   │   │   ├── EditVoiceDialog.vue
│   │   │   │   ├── FirmwareDialog.vue
│   │   │   │   ├── FunctionDialog.vue
│   │   │   │   ├── HeaderBar.vue
│   │   │   │   ├── ManualAddDeviceDialog.vue
│   │   │   │   ├── ModelEditDialog.vue
│   │   │   │   ├── ParamDialog.vue
│   │   │   │   ├── ProviderDialog.vue
│   │   │   │   ├── TtsModel.vue
│   │   │   │   ├── VersionFooter.vue
│   │   │   │   ├── ViewPasswordDialog.vue
│   │   │   │   ├── VoiceCloneDialog.vue
│   │   │   │   ├── VoicePrintDialog.vue
│   │   │   │   └── VoiceResourceDialog.vue
│   │   │   ├── i18n
│   │   │   │   ├── en.js
│   │   │   │   ├── index.js
│   │   │   │   ├── zh_CN.js
│   │   │   │   └── zh_TW.js
│   │   │   ├── main.js
│   │   │   ├── registerServiceWorker.js
│   │   │   ├── router
│   │   │   │   └── index.js
│   │   │   ├── service-worker.js
│   │   │   ├── store
│   │   │   │   └── index.js
│   │   │   ├── styles
│   │   │   │   └── global.scss
│   │   │   ├── utils
│   │   │   │   ├── cacheViewer.js
│   │   │   │   ├── constant.js
│   │   │   │   ├── date.js
│   │   │   │   ├── format.js
│   │   │   │   └── index.js
│   │   │   └── views
│   │   │       ├── AgentTemplateManagement.vue
│   │   │       ├── DeviceManagement.vue
│   │   │       ├── DictManagement.vue
│   │   │       ├── ModelConfig.vue
│   │   │       ├── OtaManagement.vue
│   │   │       ├── ParamsManagement.vue
│   │   │       ├── ProviderManagement.vue
│   │   │       ├── ServerSideManager.vue
│   │   │       ├── TemplateQuickConfig.vue
│   │   │       ├── UserManagement.vue
│   │   │       ├── VoiceCloneManagement.vue
│   │   │       ├── VoicePrint.vue
│   │   │       ├── VoiceResourceManagement.vue
│   │   │       ├── auth.scss
│   │   │       ├── home.vue
│   │   │       ├── login.vue
│   │   │       ├── register.vue
│   │   │       ├── retrievePassword.vue
│   │   │       └── roleConfig.vue
│   │   └── vue.config.js
│   └── xiaozhi-server
│       ├── agent-base-prompt.txt
│       ├── app.py
│       ├── config
│       │   ├── assets
│       │   │   ├── bind_code
│       │   │   │   ├── 0.wav
│       │   │   │   ├── 1.wav
│       │   │   │   ├── 2.wav
│       │   │   │   ├── 3.wav
│       │   │   │   ├── 4.wav
│       │   │   │   ├── 5.wav
│       │   │   │   ├── 6.wav
│       │   │   │   ├── 7.wav
│       │   │   │   ├── 8.wav
│       │   │   │   └── 9.wav
│       │   │   ├── bind_code.wav
│       │   │   ├── bind_not_found.wav
│       │   │   ├── max_output_size.wav
│       │   │   ├── tts_notify.mp3
│       │   │   ├── wakeup_words
│       │   │   │   └── ed76d459636c2481aec828516c1b4f54.wav
│       │   │   ├── wakeup_words.wav
│       │   │   └── wakeup_words_short.wav
│       │   ├── config_loader.py
│       │   ├── logger.py
│       │   ├── manage_api_client.py
│       │   └── settings.py
│       ├── config.yaml
│       ├── config_from_api.yaml
│       ├── core
│       │   ├── api
│       │   │   ├── base_handler.py
│       │   │   ├── ota_handler.py
│       │   │   └── vision_handler.py
│       │   ├── auth.py
│       │   ├── connection.py
│       │   ├── handle
│       │   │   ├── abortHandle.py
│       │   │   ├── helloHandle.py
│       │   │   ├── intentHandler.py
│       │   │   ├── receiveAudioHandle.py
│       │   │   ├── reportHandle.py
│       │   │   ├── sendAudioHandle.py
│       │   │   ├── textHandle.py
│       │   │   ├── textHandler
│       │   │   │   ├── abortMessageHandler.py
│       │   │   │   ├── helloMessageHandler.py
│       │   │   │   ├── iotMessageHandler.py
│       │   │   │   ├── listenMessageHandler.py
│       │   │   │   ├── mcpMessageHandler.py
│       │   │   │   └── serverMessageHandler.py
│       │   │   ├── textMessageHandler.py
│       │   │   ├── textMessageHandlerRegistry.py
│       │   │   ├── textMessageProcessor.py
│       │   │   └── textMessageType.py
│       │   ├── http_server.py
│       │   ├── providers
│       │   │   ├── asr
│       │   │   │   ├── aliyun.py
│       │   │   │   ├── aliyun_stream.py
│       │   │   │   ├── baidu.py
│       │   │   │   ├── base.py
│       │   │   │   ├── doubao.py
│       │   │   │   ├── doubao_stream.py
│       │   │   │   ├── dto
│       │   │   │   │   └── dto.py
│       │   │   │   ├── fun_local.py
│       │   │   │   ├── fun_server.py
│       │   │   │   ├── openai.py
│       │   │   │   ├── qwen3_asr_flash.py
│       │   │   │   ├── sherpa_onnx_local.py
│       │   │   │   ├── tencent.py
│       │   │   │   ├── vosk.py
│       │   │   │   └── xunfei_stream.py
│       │   │   ├── intent
│       │   │   │   ├── base.py
│       │   │   │   ├── function_call
│       │   │   │   │   └── function_call.py
│       │   │   │   ├── intent_llm
│       │   │   │   │   └── intent_llm.py
│       │   │   │   └── nointent
│       │   │   │       └── nointent.py
│       │   │   ├── llm
│       │   │   │   ├── AliBL
│       │   │   │   │   └── AliBL.py
│       │   │   │   ├── base.py
│       │   │   │   ├── coze
│       │   │   │   │   └── coze.py
│       │   │   │   ├── dify
│       │   │   │   │   └── dify.py
│       │   │   │   ├── fastgpt
│       │   │   │   │   └── fastgpt.py
│       │   │   │   ├── gemini
│       │   │   │   │   └── gemini.py
│       │   │   │   ├── homeassistant
│       │   │   │   │   └── homeassistant.py
│       │   │   │   ├── ollama
│       │   │   │   │   └── ollama.py
│       │   │   │   ├── openai
│       │   │   │   │   └── openai.py
│       │   │   │   ├── system_prompt.py
│       │   │   │   └── xinference
│       │   │   │       └── xinference.py
│       │   │   ├── memory
│       │   │   │   ├── base.py
│       │   │   │   ├── mem0ai
│       │   │   │   │   └── mem0ai.py
│       │   │   │   ├── mem_local_short
│       │   │   │   │   └── mem_local_short.py
│       │   │   │   └── nomem
│       │   │   │       └── nomem.py
│       │   │   ├── tools
│       │   │   │   ├── __init__.py
│       │   │   │   ├── base
│       │   │   │   │   ├── __init__.py
│       │   │   │   │   ├── tool_executor.py
│       │   │   │   │   └── tool_types.py
│       │   │   │   ├── device_iot
│       │   │   │   │   ├── __init__.py
│       │   │   │   │   ├── iot_descriptor.py
│       │   │   │   │   ├── iot_executor.py
│       │   │   │   │   └── iot_handler.py
│       │   │   │   ├── device_mcp
│       │   │   │   │   ├── __init__.py
│       │   │   │   │   ├── mcp_client.py
│       │   │   │   │   ├── mcp_executor.py
│       │   │   │   │   └── mcp_handler.py
│       │   │   │   ├── mcp_endpoint
│       │   │   │   │   ├── __init__.py
│       │   │   │   │   ├── mcp_endpoint_client.py
│       │   │   │   │   ├── mcp_endpoint_executor.py
│       │   │   │   │   └── mcp_endpoint_handler.py
│       │   │   │   ├── server_mcp
│       │   │   │   │   ├── __init__.py
│       │   │   │   │   ├── mcp_client.py
│       │   │   │   │   ├── mcp_executor.py
│       │   │   │   │   └── mcp_manager.py
│       │   │   │   ├── server_plugins
│       │   │   │   │   ├── __init__.py
│       │   │   │   │   └── plugin_executor.py
│       │   │   │   ├── unified_tool_handler.py
│       │   │   │   └── unified_tool_manager.py
│       │   │   ├── tts
│       │   │   │   ├── alibl_stream.py
│       │   │   │   ├── aliyun.py
│       │   │   │   ├── aliyun_stream.py
│       │   │   │   ├── base.py
│       │   │   │   ├── cozecn.py
│       │   │   │   ├── custom.py
│       │   │   │   ├── default.py
│       │   │   │   ├── doubao.py
│       │   │   │   ├── dto
│       │   │   │   │   └── dto.py
│       │   │   │   ├── edge.py
│       │   │   │   ├── fishspeech.py
│       │   │   │   ├── gpt_sovits_v2.py
│       │   │   │   ├── gpt_sovits_v3.py
│       │   │   │   ├── huoshan_double_stream.py
│       │   │   │   ├── index_stream.py
│       │   │   │   ├── linkerai.py
│       │   │   │   ├── minimax_httpstream.py
│       │   │   │   ├── openai.py
│       │   │   │   ├── paddle_speech.py
│       │   │   │   ├── siliconflow.py
│       │   │   │   ├── tencent.py
│       │   │   │   ├── ttson.py
│       │   │   │   └── xunfei_stream.py
│       │   │   ├── vad
│       │   │   │   ├── base.py
│       │   │   │   └── silero.py
│       │   │   └── vllm
│       │   │       ├── base.py
│       │   │       └── openai.py
│       │   ├── utils
│       │   │   ├── asr.py
│       │   │   ├── auth.py
│       │   │   ├── cache
│       │   │   │   ├── config.py
│       │   │   │   ├── manager.py
│       │   │   │   └── strategies.py
│       │   │   ├── current_time.py
│       │   │   ├── dialogue.py
│       │   │   ├── intent.py
│       │   │   ├── llm.py
│       │   │   ├── memory.py
│       │   │   ├── modules_initialize.py
│       │   │   ├── opus_encoder_utils.py
│       │   │   ├── output_counter.py
│       │   │   ├── p3.py
│       │   │   ├── prompt_manager.py
│       │   │   ├── textUtils.py
│       │   │   ├── tts.py
│       │   │   ├── util.py
│       │   │   ├── vad.py
│       │   │   ├── vllm.py
│       │   │   ├── voiceprint_provider.py
│       │   │   └── wakeup_word.py
│       │   └── websocket_server.py
│       ├── docker-compose.yml
│       ├── docker-compose_all.yml
│       ├── mcp_server_settings.json
│       ├── models
│       │   ├── SenseVoiceSmall
│       │   │   ├── chn_jpn_yue_eng_ko_spectok.bpe.model
│       │   │   ├── config.yaml
│       │   │   ├── configuration.json
│       │   │   ├── demo.py
│       │   │   └── example
│       │   │       ├── en.mp3
│       │   │       ├── ja.mp3
│       │   │       ├── ko.mp3
│       │   │       ├── yue.mp3
│       │   │       └── zh.mp3
│       │   └── snakers4_silero-vad
│       │       ├── hubconf.py
│       │       └── src
│       │           └── silero_vad
│       │               ├── __init__.py
│       │               ├── data
│       │               │   ├── __init__.py
│       │               │   ├── silero_vad.jit
│       │               │   ├── silero_vad.onnx
│       │               │   ├── silero_vad_16k_op15.onnx
│       │               │   └── silero_vad_half.onnx
│       │               ├── model.py
│       │               └── utils_vad.py
│       ├── music
│       │   ├── 一念千年_国风版.mp3
│       │   ├── 中秋月.mp3
│       │   └── 廉波老矣，尚能饭否.mp3
│       ├── performance_tester
│       │   ├── performance_tester_asr.py
│       │   ├── performance_tester_llm.py
│       │   ├── performance_tester_stream_asr.py
│       │   ├── performance_tester_stream_tts.py
│       │   ├── performance_tester_tts.py
│       │   └── performance_tester_vllm.py
│       ├── performance_tester.py
│       ├── plugins_func
│       │   ├── functions
│       │   │   ├── change_role.py
│       │   │   ├── get_news_from_chinanews.py
│       │   │   ├── get_news_from_newsnow.py
│       │   │   ├── get_time.py
│       │   │   ├── get_weather.py
│       │   │   ├── handle_exit_intent.py
│       │   │   ├── hass_get_state.py
│       │   │   ├── hass_init.py
│       │   │   ├── hass_play_music.py
│       │   │   ├── hass_set_state.py
│       │   │   └── play_music.py
│       │   ├── loadplugins.py
│       │   └── register.py
│       ├── requirements.txt
│       └── test
│           ├── abbreviated_version
│           │   ├── app.js
│           │   └── test.html
│           ├── default-mcp-tools.json
│           ├── js
│           │   ├── StreamingContext.js
│           │   ├── document.js
│           │   ├── opus.js
│           │   ├── utils
│           │   │   ├── BlockingQueue.js
│           │   │   └── logger.js
│           │   └── xiaoZhiConnect.js
│           ├── libopus.js
│           ├── opus_test
│           │   ├── app.js
│           │   └── test.html
│           ├── test_page.css
│           └── test_page.html
└── tree.md

249 directories, 885 files
