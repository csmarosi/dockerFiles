FROM debian:sid

RUN apt-get update && \
    echo wireshark-common	wireshark-common/install-setuid	boolean	false | debconf-set-selections && \
    apt-get install --no-install-recommends -y -q \
        tor iptables \
        openvpn \
        curl dnsutils tshark wget \
        tor-arm \
        tor-geoipdb \
        obfsproxy \
        procps vim \
        python3 python3-requests \
        libssl-dev gcc \
        python3-pip python3-setuptools python3-dev \
    && \
    apt-get clean

RUN pip3 install wheel && \
    pip3 install pexpect && \
    pip3 install mitmproxy==2.0.2

ENV TERM=linux TERMINFO=/etc/terminfo LANG=en_US.UTF-8

COPY root_tor/setupHacks.sh /root/
ENTRYPOINT ["/root/setupHacks.sh"]
