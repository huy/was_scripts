import sys

global AdminConfig
global AdminControl
global AdminApp

nodeName = 'FCASAWNODE02'
serverName = 'connect21'

AdminTask.deleteServer('[-serverName ' + serverName  + ' -nodeName ' + nodeName + ']')

AdminConfig.save()

