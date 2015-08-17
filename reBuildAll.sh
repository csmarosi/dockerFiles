#!/bin/bash
set -x
set -e

for image in $(git grep '[F]ROM' | cut -d' ' -f2 | sort | uniq); do
    sudo docker pull ${image}
done

for myImage in $(git ls-files | awk -F/ '/Dockerfile/ {print $1}'); do
    ./build.sh --no-cache ${myImage}
done
