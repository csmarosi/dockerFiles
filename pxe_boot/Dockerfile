FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        dnsmasq \
    && \
    apt-get clean

COPY pxe_boot/tftpboot /tftpboot
COPY pxe_boot/dnsmasq.conf /etc/
COPY pxe_boot/entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
