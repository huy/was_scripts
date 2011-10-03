. ./create_sandbox_env.sh

PROFILE_NAME=node01
NODE_NAME=$PROFILE_NAME

rm -rf $PROFILE_ROOT/$PROFILE_NAME

$APP_SERVER_ROOT/bin/wasprofile.sh -create \
-profileName $PROFILE_NAME \
-profilePath $PROFILE_ROOT/$PROFILE_NAME \
-templatePath $APP_SERVER_ROOT/profileTemplates/managed \
-cellName TO_BE_FEDERATED \
-hostName $HOST_NAME \
-nodeName $NODE_NAME 

$PROFILE_ROOT/$PROFILE_NAME/bin/addNode.sh jpsaswsi34 10306 \
-nodeagentshortname agent01 \
-startingport 10323 
