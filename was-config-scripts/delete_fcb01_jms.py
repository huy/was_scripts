node = AdminConfig.getid('/Node:FCBSAWNODE01/')
print node

cfList = AdminConfig.list('MQQueueConnectionFactory',node)

print cfList
if len(cfList) > 0:
  cfList = cfList.split("\n")
  for cf in cfList:
    AdminConfig.remove(cf)

qList = AdminConfig.list('MQQueue',node)
print qList

if len(qList) >0: 
  qList = qList.split("\n")
  for q in qList:
    AdminConfig.remove(q)

AdminConfig.save()
