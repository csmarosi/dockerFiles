sudo docker rm $(sudo docker ps -a -q)
sudo docker rmi $(sudo docker images 2>&1 | grep '^<none>' | awk '{print $3}')
