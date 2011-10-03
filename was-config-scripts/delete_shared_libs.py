
cell = AdminConfig.getid('/Cell:APPSAWCELL01/')
print cell

listLibs = AdminConfig.list('Library',cell)

if len(listLibs) > 0:
  for lib in  listLibs.split("\n"):
     AdminConfig.remove(lib)

AdminConfig.save()
