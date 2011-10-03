global AdminTask
global AdminConfig

from set_server_port import *
from set_jvm_param import *

nodeName = 'node01'
serverName = 'connect01'
startingPort = 10363
hostName='jpsaswsi34'

setServerPort(adminTask=AdminTask,
            nodeName=nodeName,
            serverName=serverName,
            hostName=hostName,
            startingPort=startingPort)

setJVMParam(adminConfig=AdminConfig,
            nodeName=nodeName,
            serverName=serverName,
            jvmId='2',
            userHome='/sit/home/flexapp/connect/system/home',
            wsExtDirs='/sit/home/flexapp/connect/system/build/classes:/sit/home/flexapp/connect/system/build/extclasses/jars:/sit/home/flexapp/connect/system/build/extclasses/FCRJars:/sit/home/flexapp/connect/fcrconfig/FCR.CONFIG')

AdminConfig.save()
