chgrp  iflex /sit/usr/IBM/WebSphere/AppServer/logs/wasprofile
chmod  g+wr  /sit/usr/IBM/WebSphere/AppServer/logs/wasprofile
chgrp  iflex /sit/usr/IBM/WebSphere/AppServer/properties
chmod  g+wr  /sit/usr/IBM/WebSphere/AppServer/properties

mkdir -p /sit/usr/IBM/WebSphere/AppServer/properties/fsdb
chgrp  iflex /sit/usr/IBM/WebSphere/AppServer/properties/fsdb
chmod  g+wr  /sit/usr/IBM/WebSphere/AppServer/properties/fsdb

chgrp  -f iflex /sit/usr/IBM/WebSphere/AppServer/properties/profileRegistry.xml
chmod  -f g+wr  /sit/usr/IBM/WebSphere/AppServer/properties/profileRegistry.xml
chgrp -R iflex /sit/usr/IBM/WebSphere/AppServer/profileTemplates

