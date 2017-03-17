FROM debian:sid

RUN apt-get update && \
    echo wireshark-common	wireshark-common/install-setuid	boolean	false | debconf-set-selections && \
    apt-get install --no-install-recommends -y -q \
        wireshark namebench dnsutils \
        tcptraceroute netcat-traditional \
        youtube-dl \
    && \
    apt-get clean

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
