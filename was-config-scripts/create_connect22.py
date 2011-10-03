global AdminConfig
global AdminTask

cluster = AdminConfig.getid('/ServerCluster:connect/')
print cluster

node = AdminConfig.getid('/Node:FCASAWNODE02/')
print node

AdminConfig.createClusterMember(cluster, node, [['memberName', 'connect22']])

AdminConfig.save()

