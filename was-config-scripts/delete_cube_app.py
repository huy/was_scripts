list = AdminApp.list().split("\n")

for appname in list:
  if appname.find('FCB')==0:
     AdminApp.uninstall(appname)

AdminConfig.save()
