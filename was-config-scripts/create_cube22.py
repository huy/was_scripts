global AdminConfig
global AdminTask

cluster = AdminConfig.getid('/ServerCluster:cube20/')
print cluster

node = AdminConfig.getid('/Node:FCBSAWNODE02/')
print node

AdminConfig.createClusterMember(cluster, node, [['memberName', 'cube22']])

AdminConfig.save()

