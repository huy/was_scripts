
jdbc = AdminConfig.getid('/Node:FCASAWNODE02/JDBCProvider:connect/')

print jdbc

AdminConfig.remove(jdbc)

AdminConfig.save()
