SCRIPTS_HOME=/backup/setup
MEDIA_HOME=/backup/upgradefiles/installer61019

umask 022

$MEDIA_HOME/UpdateInstaller/install -options $SCRIPTS_HOME/installer61019-resp.txt -silent
