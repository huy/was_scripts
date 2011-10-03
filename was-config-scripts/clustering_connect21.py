global AdminConfig

server = AdminConfig.getid('/Cell:APPSAWCELL01/Node:FCASAWNODE02/Server:connect21/')

print server

AdminConfig.convertToCluster(server, 'connect')

AdminConfig.save()
