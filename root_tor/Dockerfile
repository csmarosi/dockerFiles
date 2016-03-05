FROM debian:sid

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        tor iptables \
        curl tshark \
        tor-arm \
        tor-geoipdb \
        procps \
    && \
    apt-get clean

ENV TERM=linux TERMINFO=/etc/terminfo

COPY root_tor/setupHacks.sh /root/
ENTRYPOINT ["/root/setupHacks.sh"]
