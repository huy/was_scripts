vhost =  AdminConfig.getid('/Cell:APPSAWCELL01/VirtualHost:FCA/')
AdminConfig.remove(vhost)

vhost =  AdminConfig.getid('/Cell:APPSAWCELL01/VirtualHost:FCB/')
AdminConfig.remove(vhost)

AdminConfig.save()

