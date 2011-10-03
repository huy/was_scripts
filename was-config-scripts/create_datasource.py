def createDataSource(adminConfig, jdbc, name, jndiName, desc, url):
  nameAttr = ['name', name ]
  jndiAttr = ['jndiName', jndiName ]
  helperAttr = ['datasourceHelperClassname','com.ibm.websphere.rsadapter.Oracle10gDataStoreHelper']
  descAttr = ['description', desc]
  dsAttrs = [nameAttr,descAttr,jndiAttr,helperAttr]

  template = adminConfig.listTemplates('DataSource','Oracle JDBC Driver DataSource')
  print template

  ds = adminConfig.createUsingTemplate('DataSource', jdbc, dsAttrs, template)

  propset = adminConfig.list('J2EEResourcePropertySet',ds)

  print propset

  urlAttr = [['name','URL'],['type','java.lang.String'],['value',url]]
  adminConfig.create('J2EEResourceProperty', propset, urlAttr)

