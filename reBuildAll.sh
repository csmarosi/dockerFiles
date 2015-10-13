#!/bin/bash
set -x
set -e

baseImages=$(git grep '[F]ROM' | cut -d' ' -f2 | sort | uniq)
imagesToBuild=$(echo ${baseImages} | tr ' ' '\n' | grep  -E $(git ls-files | awk -F/ '/Dockerfile/{print "^"$1"$"}' | tr '\n' '|')GrepFiller)
imagesToPull=$( echo ${baseImages} | tr ' ' '\n' | grep -vE $(git ls-files | awk -F/ '/Dockerfile/{print "^"$1"$"}' | tr '\n' '|')GrepFiller)

for image in ${imagesToPull}; do
    docker pull ${image}
done

for myImage in ${imagesToBuild}; do
    ./build.sh ${myImage}
done

for myImage in $(git ls-files | awk -F/ '/Dockerfile/ {print $1}'); do
    ./build.sh ${myImage} || true
done
