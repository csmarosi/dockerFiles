PXE boot environment, works with SystemRescueCd.
To run it with SystemRescueCd, issue:
    docker run -it --rm --net=host -v /mnt/hd1:/cdrom:ro pxe_boot

Ubuntu netboot:
    docker run -it --rm --net=host -v /mnt/netboot:/tftpboot:ro pxe_boot
