global AdminTask
global AdminConfig

from set_server_port import *
from set_jvm_param import *

nodeName = 'FCASAWNODE02'
serverName = 'connect21'
startingPort = 10343
hostName='jpsasfap32'

setServerPort(adminTask=AdminTask,
            nodeName=nodeName,
            serverName=serverName,
            hostName=hostName,
            startingPort=startingPort)

setJVMParam(adminConfig=AdminConfig,
            nodeName=nodeName,
            serverName=serverName,
            jvmId='111',
            userHome='/sit/home/flexapp/FCCONNECT/system/home',
            wsExtDirs='/sit/home/flexapp/FCCONNECT/system/build/classes:/sit/home/flexapp/FCCONNECT/system/build/extclasses/jars:/sit/home/flexapp/FCCONNECT/system/build/extclasses/FCRJars:/sit/home/flexapp/FCCONNECT/fcrconfig/FCR.CONFIG')

AdminConfig.save()
