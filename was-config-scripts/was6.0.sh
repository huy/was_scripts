SCRIPTS_HOME=/sit/usr/setup/scripts
MEDIA_HOME=/sit/usr/setup/was6.0
JAVA_HOME=$MEDIA_HOME/JDK/repository/prereq.jdk/java

umask 022

$MEDIA_HOME/WAS/install -options $SCRIPTS_HOME/was6.0-resp.txt -silent
