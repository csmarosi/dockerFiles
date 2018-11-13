#!/bin/bash
set -euxo pipefail

baseImages=$(git grep '[F]ROM' | cut -d' ' -f2 | sort | uniq)
imagesToBuild=$(echo ${baseImages} | tr ' ' '\n' | grep -E $(git ls-files | awk -F/ '/Dockerfile/{print "^"$1"$"}' | tr '\n' '|')GrepFiller || true)
imagesToPull=$(echo ${baseImages} | tr ' ' '\n' | grep -vE $(git ls-files | awk -F/ '/Dockerfile/{print "^"$1"$"}' | tr '\n' '|')GrepFiller)

createMissing=false
echo ${@} | grep -q -- --all && createMissing=true
generateOnly=false
echo ${@} | grep -q -- --generateOnly && generateOnly=true
pullOnly=true
echo ${@} | grep -q -- --build && pullOnly=false

existingImages="$(docker images | awk '/latest/{print $1":"$2}')"
for image in ${imagesToPull}; do
    echo "${existingImages}" | grep -qw ${image} || ${createMissing} &&
        (${generateOnly} || docker pull ${image})
done

if echo ${@} | grep -q -- --pullOnly; then
    exit 0
fi

for myImage in ${imagesToBuild}; do
    echo "${existingImages}" | grep -qw ${myImage} || ${createMissing} &&
        ./build.sh ${myImage} $(${generateOnly} && echo --generateOnly)
done

${pullOnly} && exit 0

for myImage in $(git ls-files | awk -F/ '/Dockerfile/ {print $1}'); do
    echo "${existingImages}" | grep -qw ${myImage} || ${createMissing} &&
        ./build.sh ${myImage} $(${generateOnly} && echo --generateOnly) || true
done
