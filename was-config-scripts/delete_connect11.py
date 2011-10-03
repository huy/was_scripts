import sys

global AdminConfig
global AdminControl
global AdminApp

nodeName = 'FCASAWNODE01'
serverName = 'connect11'

AdminTask.deleteServer('[-serverName ' + serverName  + ' -nodeName ' + nodeName + ']')

AdminConfig.save()

