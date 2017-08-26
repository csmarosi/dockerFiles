FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        tor iptables \
        tor-arm tor-geoipdb obfsproxy \
        openvpn \
        procps vim \
        python3 python3-requests \
        libssl-dev gcc \
        python3-pip python3-setuptools python3-dev \
        youtube-dl \
        tcptraceroute netcat-traditional \
        tshark wireshark \
        curl dnsutils wget echoping namebench \
    && \
    apt-get clean

RUN pip3 install wheel && \
    pip3 install pexpect && \
    pip3 install mitmproxy==2.0.2

ENV TERM=linux TERMINFO=/etc/terminfo LANG=en_US.UTF-8

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
