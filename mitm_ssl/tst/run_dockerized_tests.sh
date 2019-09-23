#!/bin/bash
set -euxo pipefail

gitRoot=$(git rev-parse --show-toplevel)
tmpDir=$(mktemp -d)
chmod 777 ${tmpDir}

docker kill xrdp_mitm || true
docker kill mitm_test || true
docker kill selenium_mitm || true

#Run an RDP server to expose the X11 socket
docker run --name=xrdp_mitm --rm -it -d -u=$(id -u):$(id -g) \
    --net=host \
    -e HOME=/tmp \
    -v ${tmpDir}:/tmp \
    -v /etc/passwd:/etc/passwd:ro -v /etc/group:/etc/group:ro \
    xrdp_xmonad
#Actually start X11
if true; then
    docker exec xrdp_mitm X11rdp :10 -auth .Xauthority -geometry 800x600 -depth 24 -bs -nolisten tcp -uds &
else
    echo Connect manually and inspect the failing TC
    sleep 15
fi

#Run the mitm code
docker run --name=mitm_test --rm -it -d -u=$(id -u):$(id -g) \
    -e HOME=/tmp \
    -v ${gitRoot}:/dockerFiles \
    -v /etc/passwd:/etc/passwd:ro -v /etc/group:/etc/group:ro \
    --entrypoint=/usr/bin/python3 mitm_ssl \
    /dockerFiles/mitm_ssl/tst/proxy_manager.py

#Run selenium
docker run --name=selenium_mitm --rm -it --cpuset-cpus=0 -u=$(id -u):$(id -g) \
    --net=container:mitm_test \
    --shm-size 768M \
    -e DISPLAY=:10 -v ${tmpDir}/.X11-unix/X10:/tmp/.X11-unix/X10:ro \
    -e HOME=/tmp \
    -e LANG=en_US.UTF-8 -e JAVA_OPTS="-Dfile.encoding=UTF-8" \
    -v ${gitRoot}/mitm_ssl/tst:/mitm_test \
    -v /etc/passwd:/etc/passwd:ro -v /etc/group:/etc/group:ro \
    chromium_selenium_gui \
    /mitm_test/selenium.sh
