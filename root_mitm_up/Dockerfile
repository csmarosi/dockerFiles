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
        python3 \
        mitmproxy \
    && \
    apt-get clean

ENV TERM=linux TERMINFO=/etc/terminfo LANG=en_US.UTF-8

COPY root_mitm_up/upgrade.py /root/
ENTRYPOINT ["mitmdump", "-p", "8080", "-s", "/root/upgrade.py", "--ignore", "."]
