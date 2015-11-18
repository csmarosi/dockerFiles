FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        openvpn dnsutils \
        wget curl \
    && \
    apt-get clean

COPY root_openvpn/setupHacks.sh /root/

ENTRYPOINT ["/root/setupHacks.sh"]
