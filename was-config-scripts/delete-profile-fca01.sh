. ./create-profile-env.sh

PROFILE_NAME=FCASAWNODE01

$PROFILE_ROOT/$PROFILE_NAME/bin/removeNode.sh

$APP_SERVER_ROOT/bin/wasprofile.sh -delete -profileName $PROFILE_NAME 
