earDir = '/sit/home/flexapp/ears/CUBE'
clusterName = 'cube10'

cluster = AdminConfig.getid('/ServerCluster:' + clusterName + '/')
print cluster 

AdminApp.install(earDir + '/FCBINGN1SITAdhocUpload.ear','[-appname FCBAdhocUpload -cluster ' +  clusterName + ']')
AdminApp.install(earDir + '/FCBINGN1SITBATCH.ear','[-appname FCBBatch -cluster ' + clusterName + ']')
AdminApp.install(earDir + '/FCBINGN1SITGefuProcessor.ear','[-appname FCBGetfuProcessor -cluster ' + clusterName + ']')
AdminApp.install(earDir + '/FCBINGN1SITGefuScheduler.ear','[-appname FCBGetfuScheduler -cluster ' + clusterName + ']')
AdminApp.install(earDir + '/FCBINGN1SITMNT.ear',
  '[-appname FCBMNT -cluster ' + clusterName + '  -MapWebModToVH [["Apache-SOAP" soap.war,WEB-INF/web.xml FCB ] ]]')
AdminApp.install(earDir + '/FCBINGN1SITOLTP.ear','[-appname FCBOLTP -cluster ' + clusterName + ']')
AdminApp.install(earDir + '/FCBINGN1SITReport.ear','[-appname FCBReport -cluster ' + clusterName + ']')
AdminApp.install(earDir + '/FCRJAppWebService.ear',
  '[-appname FCBAppWebService -cluster ' + clusterName + '  -MapWebModToVH [["FLEXCUBE Web Application" FCRJAppWebServiceWeb.war,WEB-INF/web.xml FCA ] ]]')

AdminConfig.save()
