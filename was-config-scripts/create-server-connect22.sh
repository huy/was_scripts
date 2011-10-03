. ./create-profile-env.sh

NODE_NAME=FCASAWNODE0A
PROFILE_NAME=connect22

rm -rf $PROFILE_ROOT/standalone/$PROFILE_NAME

$APP_SERVER_ROOT/bin/wasprofile.sh -create \
-profileName $PROFILE_NAME \
-profilePath $PROFILE_ROOT/standalone/$PROFILE_NAME \
-templatePath $APP_SERVER_ROOT/profileTemplates/default \
-cellName TO_BE_FEDERATED \
-hostName $HOST_NAME \
-nodeName $NODE_NAME \
-startingPort 10363 
