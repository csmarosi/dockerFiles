FROM debian:sid

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        tor iptables \
        openvpn \
        curl dnsutils tshark wget \
        tor-arm \
        tor-geoipdb \
        obfsproxy \
        procps vim \
        python3 \
        mitmproxy \
    && \
    apt-get clean

ENV TERM=linux TERMINFO=/etc/terminfo LANG=en_US.UTF-8

COPY root_tor/setupHacks.sh /root/
ENTRYPOINT ["/root/setupHacks.sh"]
