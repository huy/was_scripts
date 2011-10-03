def setPort(adminTask,nodeName,serverName,hostName,endPoint,port):
  adminTask.modifyServerPort(serverName, '[-nodeName ' + nodeName +
                                        ' -endPointName ' + endPoint +
                                        ' -host ' + hostName +
                                        ' -port ' + str(port) + ']')

def setServerPort(adminTask,nodeName,serverName,hostName,startingPort):
  setPort(adminTask,nodeName,serverName,hostName,'BOOTSTRAP_ADDRESS',startingPort)
  setPort(adminTask,nodeName,serverName,hostName,'SOAP_CONNECTOR_ADDRESS',startingPort+1)
  setPort(adminTask,nodeName,serverName,hostName,'WC_defaulthost',startingPort+3)
  setPort(adminTask,nodeName,serverName,hostName,'WC_defaulthost_secure',startingPort+4)
  setPort(adminTask,nodeName,serverName,hostName,'WC_adminhost',startingPort+5)
  setPort(adminTask,nodeName,serverName,hostName,'WC_adminhost_secure',startingPort+6)

  setPort(adminTask,nodeName,serverName,hostName,'SAS_SSL_SERVERAUTH_LISTENER_ADDRESS',startingPort+7)
  setPort(adminTask,nodeName,serverName,hostName,'CSIV2_SSL_SERVERAUTH_LISTENER_ADDRESS',startingPort+8)
  setPort(adminTask,nodeName,serverName,hostName,'CSIV2_SSL_MUTUALAUTH_LISTENER_ADDRESS',startingPort+9)
  #setPort(adminTask,,'DCS_UNICAST_ADDRESS',startingPort+10) - share can not be changed

  adminTask.modifyServerPort(serverName, '[-modifyShared -nodeName ' + nodeName +
                                        ' -endPointName DCS_UNICAST_ADDRESS'
                                        ' -host ' + hostName +
                                        ' -port ' + str(startingPort+10) + ']')

  setPort(adminTask,nodeName,serverName,hostName,'ORB_LISTENER_ADDRESS',startingPort+11)

  setPort(adminTask,nodeName,serverName,hostName,'SIB_ENDPOINT_ADDRESS',startingPort+12)
  setPort(adminTask,nodeName,serverName,hostName,'SIB_ENDPOINT_SECURE_ADDRESS',startingPort+13)
  setPort(adminTask,nodeName,serverName,hostName,'SIB_MQ_ENDPOINT_ADDRESS',startingPort+14)
  setPort(adminTask,nodeName,serverName,hostName,'SIB_MQ_ENDPOINT_SECURE_ADDRESS',startingPort+15)
