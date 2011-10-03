global AdminTask
global AdminConfig

from set_server_port import *
from set_jvm_param import *

nodeName = 'FCBSAWNODE01'
serverName = 'cube11'
startingPort = 10403
hostName='jpsasfap31'

setServerPort(adminTask=AdminTask,
            nodeName=nodeName,
            serverName=serverName,
            hostName=hostName,
            startingPort=startingPort)

AdminConfig.save()
