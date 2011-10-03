import sys

global AdminConfig
global AdminControl
global AdminApp

nodeName = 'FCASAWNODE01'
serverName = 'Sample'
startingPort = 10340
hostName='jpsasfap32'

node = AdminConfig.getid("/Node:" + nodeName + "/")

attributes = [["name", serverName]]
server = AdminConfig.create("Server", node, attributes)

print "--- server "+ server + " created"

nameServer = AdminConfig.list("NameServer", server)
print "--- modify port for nameServer:" +  nameServer
AdminConfig.modify(nameServer, [['BOOTSTRAP_ADDRESS',[['host',hostName],['port',startingPort]] ]])

soapConnector = AdminConfig.list("SOAPConnector",server)
print "--- modify port for soapConnector:" +  soapConnector
AdminConfig.modify(soapConnector, [['SOAP_CONNECTOR_ADDRESS',[['host',hostName],['port',startingPort+1]] ]])

systemMessageServer = AdminConfig.list("SystemMessageServer",server)
if len(systemMessageServer) >0:
  print "--- modify port for systemMessageServer:" + systemMessageServer
  AdminConfig.modify(systemMessageServer, [['DRS_CLIENT_ADDRESS',[['host',hostName],['port',startingPort+2]] ]])

jmsServer = AdminConfig.list("JMSServer",server)
if len(jmsServer) >0:
  print "--- modify port for jmsServer:" + jmsServer
  AdminConfig.modify(jmsServer, [['JMSSERVER_QUEUED_ADDRESS',[['host',hostName],['port',startingPort+3]] ]])
  AdminConfig.modify(jmsServer, [['JMSSERVER_DIRECT_ADDRESS',[['host',hostName],['port',startingPort+4]] ]])
  
httpNonSecureAddress = [["sslEnabled", "false"], ["address", [["host", hostName], ["port", startingPort+5]]]]
httpSecureAddress = [["sslEnabled", "true"], ["address", [["host", hostName], ["port", startingPort+6]]], ["sslConfig", "DefaultSSLSettings"]]
transports = [["transports:HTTPTransport", [httpNonSecureAddress, httpSecureAddress]]]
webContainer = AdminConfig.list("WebContainer", server)

print "--- modify port for webContainer:" +  webContainer
AdminConfig.modify(webContainer, transports)

#exit here during test
#sys.exit()

AdminConfig.save()

nodeSync = AdminControl.completeObjectName("type=NodeSync,node=" + nodeName + ",*")
print "--- nodeSync:\n" + nodeSync

enabled = AdminControl.getAttribute(nodeSync, "serverStartupSyncEnabled")
print "--- nodeSync enabled?: \n" + enabled

if enabled == "false":
  print "--- invoking synchronization"
  AdminControl.invoke(nodeSync,"sync")

