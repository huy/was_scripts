def modifySharedLibs(appname):
  global AdminConfig
  deployment = AdminConfig.getid('/Deployment:' + appname)
  print deployment

  appDeploy = AdminConfig.showAttribute(deployment, 'deployedObject')
  print appDeploy

  classLoader = AdminConfig.showAttribute(appDeploy, 'classloader')
  print classLoader

  #AdminConfig.create('LibraryRef', classLoader, [['libraryName',libname],  ['sharedClassloader', 'true']])
  listRef = AdminConfig.list('LibraryRef', classLoader)
  if len(listRef) > 0:
    print "-- remove lib ref(s) of " + appname 
    for ref in listRef.split("\n"):
       AdminConfig.remove(ref) 
  
listApp = AdminApp.list().split("\n")
if len(listApp)>0:
  for appname in listApp:
    if appname.find('FCB')==0:
      modifySharedLibs(appname)

