SCRIPTS_HOME=/sit/usr/setup/scripts
MEDIA_HOME=/sit/usr/setup/installer6.1.0.15

umask 022

$MEDIA_HOME/UpdateInstaller/install -options $SCRIPTS_HOME/installer6.1.0.15-resp.txt -silent
