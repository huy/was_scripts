global AdminConfig
global AdminTask

nodeName = 'FCBSAWNODE01'
serverName = 'cube11'
hostName='jpsasfap31'

AdminTask.createApplicationServer(nodeName,'[-name ' + serverName + ' -templateName default]')

AdminConfig.save()

