SCRIPTS_HOME=/backup/setup
INSTALLER_HOME=/usr/IBM/UpdateInstaller6.1.0.19

umask 022

$INSTALLER_HOME/update.sh -options $SCRIPTS_HOME/pk67161-resp.txt -silent