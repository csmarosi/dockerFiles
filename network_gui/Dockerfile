FROM debian:sid

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install --no-install-recommends -y -q \
        wireshark namebench dnsutils \
        tcptraceroute netcat-traditional \
    && \
    apt-get clean

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
