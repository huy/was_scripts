global AdminTask
global AdminConfig

from set_server_port import *
from set_jvm_param import *

nodeName = 'node01'
serverName = 'webtop01'
startingPort = 10343
hostName='jpsaswsi34'

setServerPort(adminTask=AdminTask,
            nodeName=nodeName,
            serverName=serverName,
            hostName=hostName,
            startingPort=startingPort)

setJVMParam(adminConfig=AdminConfig,
            nodeName=nodeName,
            serverName=serverName,
            jvmId='1',
            userHome='/sit/home/flexapp/sandbox/webtop/system/home',
            wsExtDirs='/sit/home/flexapp/sandbox/webtop/system/build/classes:/sit/home/flexapp/sandbox/webtop/system/build/extclasses')

AdminConfig.save()
