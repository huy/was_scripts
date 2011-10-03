
mq = AdminConfig.getid('/Cell:APPSAWCELL01/Node:FCBSAWNODE01/JMSProvider:WebSphere MQ JMS Provider') 
print mq

def create_qcf(provider,name,jndiName,qm,host,port):
  global AdminConfig
  nameAttr = ['name', name]
  jndiAttr = ['jndiName', jndiName]
  qmAttr = ['queueManager', qm]
  hostAttr = ['host', host]
  portAttr = ['port', port]
  attrs = [nameAttr, jndiAttr, qmAttr, hostAttr, portAttr]
  template = AdminConfig.listTemplates('MQQueueConnectionFactory','default')
  AdminConfig.createUsingTemplate('MQQueueConnectionFactory',provider, attrs, template)


print "--- create queue connection factory"

create_qcf(mq,'FCBSITBatchQM1','jms/FCBSITBatchQM1','FCBSITBatchQM1','10.23.110.93','4364')
create_qcf(mq,'FCBSITBatchQM2','jms/FCBSITBatchQM2','FCBSITBatchQM2','10.23.110.93','4368')

create_qcf(mq,'FCBSITOltpQM1','jms/FCBSITOltpQM1','FCBSITOltpQM1','10.23.110.93','4361')
create_qcf(mq,'FCBSITOltpQM2','jms/FCBSITOltpQM2','FCBSITOltpQM2','10.23.110.93','4362')

create_qcf(mq,'FCBSITReportQM1','jms/FCBSITReportQM1','FCBSITReportQM1','10.23.110.93','4381')
create_qcf(mq,'FCBSITReportQM2','jms/FCBSITReportQM2','FCBSITReportQM2','10.23.110.93','4382')

def create_queue(provider,name,jndiName,qm,qn,host,port):
  global AdminConfig
  nameAttr = ['name', name]
  jndiAttr = ['jndiName', jndiName]
  qnAttr = ['baseQueueName', qn]
  qmAttr = ['baseQueueManagerName',qm]
  hostAttr = ['queueManagerHost',host]
  portAttr = ['queueManagerPort',port]
  attrs = [nameAttr, jndiAttr, qnAttr, qmAttr, hostAttr, portAttr]

  queue = AdminConfig.create('MQQueue', provider, attrs)

print "--- create queue"

create_queue(mq,'FCBSITBatchRequestQ1','jms/FCBSITBatchRequestQ1','FCBSITBatchQM1','FCBSITBatchRequestQ','10.23.110.93',4364)
create_queue(mq,'FCBSITBatchRequestQ2','jms/FCBSITBatchRequestQ2','FCBSITBatchQM2','FCBSITBatchRequestQ','10.23.110.93',4368)
create_queue(mq,'FCBSITBatchShellQ1','jms/FCBSITBatchShellQ1','FCBSITBatchQM1','FCBSITBatchShellQ','10.23.110.93',4364) 
create_queue(mq,'FCBSITBatchShellQ2','jms/FCBSITBatchShellQ2','FCBSITBatchQM2','FCBSITBatchShellQ','10.23.110.93',4368) 
create_queue(mq,'FCBSITBatchResponseQ','jms/FCBSITBatchResponseQ','','FCBSITBatchResponseQ','10.23.110.93',0) # strange config, ask why 

create_queue(mq,'FCBSITOltpRequestQ1','jms/FCBSITOltpRequestQ1','FCBSITOltpQM1','FCBSITOltpRequestQ','10.23.110.93',4361)
create_queue(mq,'FCBSITOltpRequestQ2','jms/FCBSITOltpRequestQ2','FCBSITOltpQM2','FCBSITOltpRequestQ','10.23.110.93',4362)
create_queue(mq,'FCBSITOltpResponseQ','jms/FCBSITOltpResponseQ','','FCBSITOltpResponseQ','10.23.110.93',0)

create_queue(mq,'FCBSITReportRequestQ1','jms/FCBSITReportRequestQ1','FCBSITReportQM1','FCBSITReportRequestQ','10.23.110.93',4381)
create_queue(mq,'FCBSITReportRequestQ2','jms/FCBSITReportRequestQ2','FCBSITReportQM2','FCBSITReportRequestQ','10.23.110.93',4382)
create_queue(mq,'FCBSITReportResponseQ','jms/FCBSITReportResponseQ','','FCBSITReportResponseQ','10.23.110.93',0)

AdminConfig.save()
