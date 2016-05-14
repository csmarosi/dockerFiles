docker rm $(docker ps -a -q)
docker rmi $(docker images 2>&1 | grep '^<none>' | awk '{print $3}')

oldImageToRm="${1}"
if [ -n "${oldImageToRm}" ]; then
    echo docker rmi \
        $(docker images | awk '{print $1":"$2}' | \
          grep "${oldImageToRm}.*201")
fi
