FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        tor iptables \
        curl tshark \
    && \
    apt-get clean

COPY root_tor/setupHacks.sh /root/
ENTRYPOINT ["/root/setupHacks.sh"]
