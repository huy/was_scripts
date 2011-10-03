global AdminConfig

cluster = AdminConfig.getid('/ServerCluster:connect/')
print cluster 

print AdminConfig.required('JDBCProvider')

nameAttr = ['name', 'connect']
implClassAttr = ['implementationClassName', 'oracle.jdbc.pool.OracleConnectionPoolDataSource']
cpAttr = ['classpath','/sit/home/flexapp/FCCONNECT/system/build/extclasses/jars/ojdbc14.jar']

jdbcAttrs = [nameAttr,implClassAttr,cpAttr]

print jdbcAttrs

jdbc = AdminConfig.create('JDBCProvider', cluster, jdbcAttrs)
print jdbc

def createDataSource(name, desc, url):
  nameAttr = ['name', name ]
  jndiAttr = ['jndiName', name ]
  helperAttr = ['datasourceHelperClassname','com.ibm.websphere.rsadaper.OracleDataStoreHelper']
  descAttr = ['description', desc]
  dsAttrs = [nameAttr,descAttr,jndiAttr,helperAttr]
  ds = AdminConfig.create('DataSource', jdbc, dsAttrs)
  propset = AdminConfig.create('J2EEResourcePropertySet',ds,[])
  urlAttr = [['name','URL'],['type','java.lang.String'],['value',url]]
  AdminConfig.create('J2EEResourceProperty', propset, urlAttr)

a1Url = 'jdbc:oracle:thin:@(DESCRIPTION_LIST=(FAILOVER=TRUE)(LOAD_BALANCE=FALSE)(DESCRIPTION=(enable=broken)(ADDRESS_LIST =(LOAD_BALANCE = ON)(FAILOVER = ON)(ADDRESS = (PROTOCOL = TCP)(HOST = jpsapfdb31-vip)(PORT = 1521)) (ADDRESS = (PROTOCOL = TCP)(HOST = jpsapfdb32-vip)(PORT = 1521)))(CONNECT_DATA =  (SERVER = DEDICATED)(SERVICE_NAME = FCBP_primary)(FAILOVER_MODE= (TYPE=SESSION)(METHOD=BASIC))))(DESCRIPTION=(enable=broken)(ADDRESS_LIST =(LOAD_BALANCE = ON)(FAILOVER = ON)(ADDRESS = (PROTOCOL = TCP)(HOST = jpsbpfdb31-vip)(PORT = 1521)) (ADDRESS = (PROTOCOL = TCP)(HOST = jpsbpfdb32-vip)(PORT = 1521)))(CONNECT_DATA =  (SERVER = DEDICATED)(SERVICE_NAME = FCBP_primary)(FAILOVER_MODE= (TYPE=SESSION)(METHOD=BASIC)))))'

fjUrl = 'jdbc:oracle:thin:@(DESCRIPTION_LIST=(FAILOVER=TRUE)(LOAD_BALANCE=FALSE)(DESCRIPTION=(enable=broken)(ADDRESS_LIST =(LOAD_BALANCE = ON)(FAILOVER = ON)(ADDRESS = (PROTOCOL = TCP)(HOST = jpsapfdb31-vip)(PORT = 1521)) (ADDRESS = (PROTOCOL = TCP)(HOST = jpsapfdb32-vip)(PORT = 1521)))(CONNECT_DATA =  (SERVER = DEDICATED)(SERVICE_NAME = FCBP_primary)(FAILOVER_MODE= (TYPE=SESSION)(METHOD=BASIC))))(DESCRIPTION=(enable=broken)(ADDRESS_LIST =(LOAD_BALANCE = ON)(FAILOVER = ON)(ADDRESS = (PROTOCOL = TCP)(HOST = jpsbpfdb31-vip)(PORT = 1521)) (ADDRESS = (PROTOCOL = TCP)(HOST = jpsbpfdb32-vip)(PORT = 1521)))(CONNECT_DATA =  (SERVER = DEDICATED)(SERVICE_NAME = FCBP_primary)(FAILOVER_MODE= (TYPE=SESSION)(METHOD=BASIC)))))'

znUrl = 'jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS_LIST =(LOAD_BALANCE = ON)(FAILOVER = ON)(ADDRESS = (PROTOCOL = TCP)(HOST = 10.23.107.110)(PORT = 1521)) (ADDRESS = (PROTOCOL = TCP)(HOST = 10.23.107.109)(PORT = 1521)))(CONNECT_DATA =  (SERVER = DEDICATED)(SERVICE_NAME = fcbs_a)(GLOBAL_NAME=fcbs_a)(FAILOVER_MODE= (TYPE=SESSION)(METHOD=BASIC))))'

createDataSource('A1','Default datasource', a1Url)
createDataSource('FJ','FJ datasource', fjUrl)
createDataSource('ZN','Zengin datasource', znUrl)

AdminConfig.save()
