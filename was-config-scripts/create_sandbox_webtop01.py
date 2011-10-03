import sys
global AdminConfig
global AdminControl
global AdminApp
global AdminTask

nodeName = 'node01'
serverName = 'webtop01'
startingPort = 10343
hostName='jpsaswsi34'

AdminTask.createApplicationServer(nodeName,'[-name ' + serverName + ' -templateName default]')

AdminConfig.save()

