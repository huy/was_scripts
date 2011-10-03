#!/bin/sh
today=`date +"%Y_%m_%d_%H_%M_%S"`
echo "#### Backs up the WebSphere profiles on the machine."
mkdir -p /backup/WAS/profiles/${today}

for profile in `ls /usr/IBM/WebSphere/AppServer/profiles`; do
  echo "## Backing up the profile: ${profile}"
  /usr/IBM/WebSphere/AppServer/bin/backupConfig.sh /backup/WAS/profiles/${today}/${profile}.zip -nostop -profileName ${profile}
  echo "## Copying the backup log file."
  cp /usr/IBM/WebSphere/AppServer/profiles/${profile}/logs/backupConfig.log /backup/WAS/profiles/${today}/${profile}_backupConfig.log
done
