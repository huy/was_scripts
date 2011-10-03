SCRIPTS_HOME=/sit/usr/setup/scripts
MEDIA_HOME=/sit/usr/setup/was6.0.2

umask 022

$MEDIA_HOME/IHS/updateinstaller/update -options $SCRIPTS_HOME/ihs6.0.2-resp.txt -silent
