global AdminTask
global AdminConfig

from set_server_port import *
from set_jvm_param import *

nodeName = 'FCBSAWNODE02'
serverName = 'cube22'
startingPort = 10423
hostName='jpsasfap32'

setServerPort(adminTask=AdminTask,
            nodeName=nodeName,
            serverName=serverName,
            hostName=hostName,
            startingPort=startingPort)

AdminConfig.save()
