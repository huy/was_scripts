import sys

global AdminConfig
global AdminControl
global AdminApp

nodeName = 'FCASAWNODE01'
serverName = 'Sample'

server = AdminConfig.getid("/Node:" + nodeName +"/Server:"+ serverName +"/")

print server

if len(server) == 0:
  print "-- server " + serverName + " not found"
  sys.exit()

AdminConfig.remove(server)

AdminConfig.save()

nodeSync = AdminControl.completeObjectName("type=NodeSync,node=" + nodeName + ",*")
print "--- nodeSync:\n" + nodeSync

enabled = AdminControl.getAttribute(nodeSync, "serverStartupSyncEnabled")
print "--- nodeSync enabled?: \n" + enabled

if enabled == "false":
  print "invoking synchronization"
  AdminControl.invoke(nodeSync,"sync")
