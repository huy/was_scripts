import sys
global AdminConfig
global AdminControl
global AdminApp
global AdminTask

nodeName = 'node01'
serverName = 'connect01'
startingPort = 10363
hostName='jpsaswsi34'

AdminTask.createApplicationServer(nodeName,'[-name ' + serverName + ' -templateName default]')

AdminConfig.save()

