SCRIPTS_HOME=/sit/usr/setup/scripts
INSTALLER_HOME=/sit/usr/IBM/UpdateInstaller6.1.0.17

umask 022

$INSTALLER_HOME/update.sh -options $SCRIPTS_HOME/plugin6.0.2.27-resp.txt -silent
