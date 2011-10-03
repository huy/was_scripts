cell = AdminConfig.getid('/Cell:APPSAWCELL01/')

template = AdminConfig.listTemplates('VirtualHost', 'default_host')

vhost = AdminConfig.createUsingTemplate('VirtualHost', cell, [['name', 'FCA']], template)
AdminConfig.modify(vhost,[ ['aliases',[[['hostname','*'],['port','*']]]] ])

vhost = AdminConfig.createUsingTemplate('VirtualHost', cell, [['name', 'FCB']], template)
AdminConfig.modify(vhost,[ ['aliases',[[['hostname','*'],['port','*']]]] ])

