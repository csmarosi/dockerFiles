FROM debian:sid

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        wireshark namebench dnsutils \
        tcptraceroute netcat-traditional \
        youtube-dl \
    && \
    apt-get clean

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
