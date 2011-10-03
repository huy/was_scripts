
jdbc = AdminConfig.getid('/JDBCProvider:connect/')

print jdbc

AdminConfig.remove(jdbc)

AdminConfig.save()
