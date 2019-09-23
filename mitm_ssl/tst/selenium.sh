#!/bin/bash
set -euxo pipefail

#Add passwordless sudo (root pwd is 'p')
echo p | su -c "echo $(whoami):$(whoami) | chpasswd"

date
#Run the TCs
pushd /opt/selenium-java/
time scala -cp *jar:lib/* >/tmp/stdout 2>/tmp/stderr <<EOF
:load /mitm_test/src/main/scala/mitm/TestMitm.scala
TestMitm.runAllLocalTest
EOF
tail -n999 /tmp/stdout

exit 0

#################################################################
# Edit/lint the selenium code
#################################################################
/opt/eclipse/eclipse -configuration /tmp/.ecxx -data /tmp/workspace -nosplash &

export GRADLE_USER_HOME=/tmp/gradle
mkdir -p $GRADLE_USER_HOME
export PATH=$PATH:/opt/gradle/gradle-4.6/bin
cd /mitm_test
gradle wrapper

gradle :scalafmtAll
