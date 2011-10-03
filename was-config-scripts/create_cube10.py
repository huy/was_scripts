global AdminConfig

server = AdminConfig.getid('/Cell:APPSAWCELL01/Node:FCBSAWNODE01/Server:cube11/')

print server

AdminConfig.convertToCluster(server, 'cube10')

AdminConfig.save()
