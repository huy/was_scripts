SCRIPTS_HOME=/sit/usr/setup/scripts
INSTALLER_HOME=/sit/usr/IBM/UpdateInstaller6.1.0.15

umask 022

$INSTALLER_HOME/update.sh -options $SCRIPTS_HOME/ihs6.0.2.27-resp.txt -silent
