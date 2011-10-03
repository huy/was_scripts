SILENT_INSTALL_HOME=/sit/usr/silent-install
WAS_INSTALL_ROOT=/sit/usr/IBM/WebSphere/AppServer

umask 022

$WAS_INSTALL_ROOT/bin/pctAIX.bin -options $SILENT_INSTALL_HOME/sit-was-create-dmgr-profile-resp.txt -silent
