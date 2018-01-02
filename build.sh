#!/bin/bash
set -euxo pipefail

buildOptions=''
if [ '--no-cache' == "${1}" ]; then
    buildOptions='--no-cache'
    shift
fi

for imageName in ${@}; do
    imageName=$(echo ${imageName} | sed 's!/!!g')
    dockerFile=${imageName}/Dockerfile
    if [ ! -f ${dockerFile} ]; then
        dockerFile=${imageName}/Dockerfile.gen
        bash ${imageName}/Dockerfile.sh > ${dockerFile}
    fi
    docker build ${buildOptions} -t ${imageName} -f ${dockerFile} .
    docker tag ${imageName} ${imageName}:$(date +%Y%m%d)
done
