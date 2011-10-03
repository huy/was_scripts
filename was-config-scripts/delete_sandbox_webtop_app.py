list = ['WebTop']

for appname in list:
  AdminApp.uninstall(appname)

AdminConfig.save()
