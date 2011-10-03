./wsadmin.sh -host jpsbdfap31 -port 8879  -lang jython

jvm = AdminControl.queryNames("WebSphere:type=JVM,process=FCBINGN1DEVServer1,node=FCBDBWNODE01,*")

AdminControl.invoke(jvm,'generateHeapDump')

 

 


