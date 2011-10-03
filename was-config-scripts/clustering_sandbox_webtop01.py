global AdminConfig

server = AdminConfig.getid('/Cell:sandbox/Node:node01/Server:webtop01/')

print server

AdminConfig.convertToCluster(server, 'webtop')

AdminConfig.save()
