#!/bin/bash
set -x
set -e

sudo debootstrap --arch=i386 --variant=minbase jessie jessie
sudo tar -C jessie -c . | docker import - debian
docker tag -f debian debian:sid
