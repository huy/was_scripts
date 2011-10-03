global AdminConfig
global AdminTask

nodeName = 'FCBSAWNODE02'
serverName = 'cube21'
hostName='jpsasfap32'

AdminTask.createApplicationServer(nodeName,'[-name ' + serverName + ' -templateName default]')

AdminConfig.save()

