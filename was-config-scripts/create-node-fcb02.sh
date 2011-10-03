. ./create-profile-env.sh

PROFILE_NAME=FCBSAWNODE02
NODE_NAME=$PROFILE_NAME

rm -rf $PROFILE_ROOT/$PROFILE_NAME

$APP_SERVER_ROOT/bin/wasprofile.sh -create \
-profileName $PROFILE_NAME \
-profilePath $PROFILE_ROOT/$PROFILE_NAME \
-templatePath $APP_SERVER_ROOT/profileTemplates/managed \
-cellName TO_BE_FEDERATED \
-hostName $HOST_NAME \
-nodeName $NODE_NAME 

$PROFILE_ROOT/$PROFILE_NAME/bin/addNode.sh jpsasfap32 10306 \
-nodeagentshortname FCBSAWNAGT02 \
-startingport 10383 
