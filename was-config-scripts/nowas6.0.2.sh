SCRIPTS_HOME=/sit/usr/setup/scripts
MEDIA_HOME=/sit/usr/setup/was6.0.2

umask 022

$MEDIA_HOME/WAS/updateinstaller_rp0000002/update -options $SCRIPTS_HOME/nowas6.0.2-resp.txt -silent
