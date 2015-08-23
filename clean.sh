docker rm $(docker ps -a -q)
docker rmi $(docker images 2>&1 | grep '^<none>' | awk '{print $3}')
