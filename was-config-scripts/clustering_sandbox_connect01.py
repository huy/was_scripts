global AdminConfig

server = AdminConfig.getid('/Cell:sandbox/Node:node01/Server:connect01/')

print server

AdminConfig.convertToCluster(server, 'connect')

AdminConfig.save()
