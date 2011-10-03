global AdminConfig
from create_datasource import *

cluster = AdminConfig.getid('/ServerCluster:connect/')
print cluster 

print AdminConfig.required('JDBCProvider')

nameAttr = ['name', 'connect']
implClassAttr = ['implementationClassName', 'oracle.jdbc.pool.OracleConnectionPoolDataSource']
cpAttr = ['classpath','/sit/home/flexapp/connect/system/build/extclasses/jars/ojdbc14.jar']

jdbcAttrs = [nameAttr,implClassAttr,cpAttr]

print jdbcAttrs

jdbc = AdminConfig.create('JDBCProvider', cluster, jdbcAttrs)
print jdbc

url = 'jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS_LIST =(LOAD_BALANCE = ON)(FAILOVER = ON)(ADDRESS = (PROTOCOL = TCP)(HOST = jpsasfdb31-vip)(PORT = 1522)) (ADDRESS = (PROTOCOL = TCP)(HOST = jpsasfdb32-vip)(PORT = 1522)))(CONNECT_DATA =  (SERVER = DEDICATED)(SERVICE_NAME = fcst_a)(GLOBAL_NAME=fcst_a)(FAILOVER_MODE= (TYPE=SESSION)(METHOD=BASIC))))'

createDataSource(AdminConfig,jdbc,'A1','A1','Default datasource', url)
createDataSource(AdminConfig,jdbc,'A2','A2','Default datasource', url)
createDataSource(AdminConfig,jdbc,'FJ','FJ','FJ datasource', url)
createDataSource(AdminConfig,jdbc,'ZN','ZN','Zengin datasource', url)

AdminConfig.save()
