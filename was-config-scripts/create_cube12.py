global AdminConfig
global AdminTask

cluster = AdminConfig.getid('/ServerCluster:cube10/')
print cluster

node = AdminConfig.getid('/Node:FCBSAWNODE01/')
print node

AdminConfig.createClusterMember(cluster, node, [['memberName', 'cube12']])

AdminConfig.save()

