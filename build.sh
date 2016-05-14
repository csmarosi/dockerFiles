#!/bin/bash
set -x
set -e

buildOptions=''
if [ '--no-cache' == "${1}" ]; then
    buildOptions='--no-cache'
    shift
fi

for imageName in ${@}; do
    imageName=$(echo ${imageName} | sed 's!/!!g')
    docker build ${buildOptions} -t ${imageName} -f ${imageName}/Dockerfile .
    docker tag -f ${imageName} ${imageName}:$(date +%Y%m%d)
done
