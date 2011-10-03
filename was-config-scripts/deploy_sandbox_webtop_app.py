cluster = AdminConfig.getid('/ServerCluster:connect/')
print cluster 

ear_dir = '/sit/home/flexapp/deployable'

list = ['WebTop']

for app in list:
  AdminApp.install( '%s/%s.ear'%(ear_dir,app),'[-appname %s -cluster webtop]' % app )
  
AdminConfig.save()

