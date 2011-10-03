def setJVMParam(adminConfig, nodeName,serverName,jvmId, userHome,wsExtDirs):
  server = adminConfig.getid('/Node:' + nodeName + '/Server:' + serverName +'/')
  print server
  jvm = adminConfig.list('JavaVirtualMachine', server)
  print jvm

  sysprops = [ 'systemProperties',
   [
    [['name','fcat.jvm.id'],['value',jvmId],['description','Id to uniquely identify a JVM']],
    [['name','user.home'],['value',userHome],['description','Home directory containing property files']],
    [['name','ws.ext.dirs'],['value',wsExtDirs], ['description','Directory path containing required classes & jars'] ]
   ]]

  adminConfig.modify(jvm, [['systemProperties',[]]])
  adminConfig.modify(jvm, [ ['initialHeapSize', 128],['maximumHeapSize',256], sysprops ])

  processDef = adminConfig.list('JavaProcessDef', server)
  processExec = adminConfig.list('ProcessExecution', processDef)

  adminConfig.modify(processExec, [['runAsUser','flexsit'],['runAsGroup','iflex']])

