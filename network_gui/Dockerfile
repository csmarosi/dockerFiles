FROM debian

RUN apt-get update && \
    echo wireshark-common	wireshark-common/install-setuid	boolean	false | debconf-set-selections && \
    apt-get install --no-install-recommends -yq \
        tor iptables \
        tor-arm tor-geoipdb obfsproxy \
        openvpn \
        procps vim \
        python3 python3-requests \
        libssl-dev gcc \
        python3-pip python3-setuptools python3-dev \
        youtube-dl openssh-client w3m \
        tcptraceroute netcat-traditional \
        tshark wireshark \
        curl dnsutils wget echoping namebench \
        make git libnet-ip-perl libio-socket-inet6-perl libnet-dns-perl tayga \
    && \
    apt-get clean

RUN pip3 install wheel && \
    pip3 install pexpect && \
    pip3 install coverage && \
    pip3 install mitmproxy==3.0.4

ENV TERM=linux TERMINFO=/etc/terminfo LANG=en_US.UTF-8

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
