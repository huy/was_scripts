. ./create-profile-env.sh

PROFILE_NAME=APPSAWDMGR01
NODE_NAME=$PROFILE_NAME

rm -rf $PROFILE_ROOT/$PROFILE_NAME

$APP_SERVER_ROOT/bin/wasprofile.sh -create \
-profileName $PROFILE_NAME \
-profilePath $PROFILE_ROOT/$PROFILE_NAME \
-templatePath $APP_SERVER_ROOT/profileTemplates/dmgr \
-cellName $CELL_NAME \
-hostName $HOST_NAME \
-nodeName $NODE_NAME \
-startingPort 10303
