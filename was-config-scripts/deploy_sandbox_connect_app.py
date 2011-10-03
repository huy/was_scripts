cluster = AdminConfig.getid('/ServerCluster:connect/')
print cluster 

ear_dir = '/sit/home/flexapp/deployable'
AdminApp.install(ear_dir + '/ChannelControllerEJB.ear','[-appname ChannelControllerEJB -cluster connect]')
AdminApp.install(ear_dir + '/ServiceLayerEJB.ear','[-appname ServiceLayerEJB -cluster connect]')
AdminApp.install(ear_dir + '/TimerBean.ear','[-appname TimerBean -cluster connect]')
AdminApp.install(ear_dir + '/TransactionBean.ear','[-appname TransactionBean -cluster connect]')
AdminApp.install(ear_dir + '/ServiceLayerSOAP.ear',
  '[-appname ServiceLayerSOAP -cluster connect -MapWebModToVH [["HTTP router for service.jar" service_HTTPRouter.war,WEB-INF/web.xml default_host] ]]')

AdminConfig.save()

