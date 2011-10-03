global AdminConfig

server = AdminConfig.getid('/Cell:APPSAWCELL01/Node:FCBSAWNODE02/Server:cube21/')

print server

AdminConfig.convertToCluster(server, 'cube20')

AdminConfig.save()
