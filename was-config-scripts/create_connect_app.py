cluster = AdminConfig.getid('/ServerCluster:connect/')
print cluster 

ear_dir = '/sit/home/flexapp/ears/CONNECT'
AdminApp.install(ear_dir + '/FCAT_ChannelController_EJB.ear','[-appname FCAChannelController -cluster connect]')
AdminApp.install(ear_dir + '/FCAT_ServiceLayer_EJB.ear','[-appname FCAServiceLayerEJB -cluster connect]')
AdminApp.install(ear_dir + '/FCAT_TimerBean.ear','[-appname FCATimer -cluster connect]')
AdminApp.install(ear_dir + '/FCAT_TransactionBean.ear','[-appname FCATransaction -cluster connect]')
AdminApp.install(ear_dir + '/FCAT_ServiceLayer_WebService.ear',
  '[-appname FCAServiceLayerWebService -cluster connect -MapWebModToVH [["HTTP router for service.jar" service_HTTPRouter.war,WEB-INF/web.xml FCA] ]]')

AdminConfig.save()

