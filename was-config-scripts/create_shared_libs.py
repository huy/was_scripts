
cell = AdminConfig.getid('/Cell:APPSAWCELL01/')
print cell

def create_lib(name,path):
  AdminConfig.create('Library', cell, [
    ['name', name], 
    ['classPath',path]
  ])

lib = '/home/flexapp/FCBSITCluster/SharedLibraries'

create_lib('FCBAdhocUpload',lib + '/FCRJAdhocUploadClient.jar')
create_lib('FCBApp',lib + '/FCRJApp.jar')
create_lib('FCBAudit', lib + '/FCRJAudit.jar')
create_lib('FCBCommon', lib + '/FCRJCommon.jar')
create_lib('FCBEntity', lib + '/FCRJEntity.jar')
create_lib('FCBGefx', lib + '/FCRJGefx.jar') 
create_lib('FCBInfra', lib + '/FCRJInfra.jar')	 
create_lib('FCBMonClient', lib + '/FCRMonitoringClient.jar') 
create_lib('FCBUploadBH', lib + '/FCRJUploadBH.jar')

AdminConfig.save()
