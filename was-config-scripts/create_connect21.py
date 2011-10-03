import sys
global AdminConfig
global AdminControl
global AdminApp
global AdminTask

nodeName = 'FCASAWNODE02'
serverName = 'connect21'
startingPort = 10343
hostName='jpsasfap32'

AdminTask.createApplicationServer(nodeName,'[-name ' + serverName + ' -templateName default]')

AdminConfig.save()

