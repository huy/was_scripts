global AdminConfig
global AdminTask

cluster = AdminConfig.getid('/ServerCluster:connect/')
print cluster

node = AdminConfig.getid('/Node:FCASAWNODE01/')
print node

AdminConfig.createClusterMember(cluster, node, [['memberName', 'connect11']])

AdminConfig.save()

