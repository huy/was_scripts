APP_SERVER_ROOT=/sit/usr/IBM/WebSphere/AppServer
PROFILE_NAME=APPSAWDMGR01

$APP_SERVER_ROOT/bin/wasprofile.sh -delete \
-profileName $PROFILE_NAME 
