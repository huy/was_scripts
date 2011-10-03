global AdminConfig
from create_datasource import *

node = AdminConfig.getid('/Node:FCBSAWNODE02/')
print  node

print AdminConfig.required('JDBCProvider')

nameAttr = ['name', 'cube']
implClassAttr = ['implementationClassName', 'oracle.jdbc.pool.OracleConnectionPoolDataSource']
cpAttr = ['classpath','/sit/home/flexapp/FCBPRODCluster/thirdpartyjars/ojdbc14.jar']

jdbcAttrs = [nameAttr,implClassAttr,cpAttr]

print jdbcAttrs

jdbc = AdminConfig.create('JDBCProvider', node, jdbcAttrs)
print jdbc

pri_url = 'jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS_LIST =(LOAD_BALANCE = ON)(FAILOVER = ON)(ADDRESS = (PROTOCOL = TCP)(HOST = 10.23.107.110)(PORT = 1521)) (ADDRESS = (PROTOCOL = TCP)(HOST = 10.23.107.109)(PORT = 1521)))(CONNECT_DATA =  (SERVER = DEDICATED)(SERVICE_NAME = fcbs_a)(GLOBAL_NAME=fcbs_a)(FAILOVER_MODE= (TYPE=SESSION)(METHOD=BASIC))))'

alt_url = 'jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS_LIST =(LOAD_BALANCE = ON)(FAILOVER = ON)(ADDRESS = (PROTOCOL = TCP)(HOST = 10.23.107.110)(PORT = 1521)) (ADDRESS = (PROTOCOL = TCP)(HOST = 10.23.107.109)(PORT = 1521)))(CONNECT_DATA =  (SERVER = DEDICATED)(SERVICE_NAME = fcbs_a)(GLOBAL_NAME=fcbs_a)(FAILOVER_MODE= (TYPE=SESSION)(METHOD=BASIC))))'

createDataSource(AdminConfig,jdbc,'FCBN1SITDataSource','jdbc/FCBN1SITDataSource','Primary datasource', pri_url)

createDataSource(AdminConfig,jdbc,'FCBN1SITAltDataSource','jdbc/FCBN1SITAltDataSource','Alternative datasource', alt_url)

AdminConfig.save()
