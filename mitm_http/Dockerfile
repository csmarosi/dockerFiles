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
        dnsmasq \
    && \
    apt-get clean

RUN pip3 install wheel && \
    pip3 install pexpect && \
    pip3 install coverage && \
    pip3 install mitmproxy==3.0.4

RUN curl -L -o cd.deb https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.deb \
    && dpkg -i cd.deb && rm cd.deb

RUN curl -L https://github.com/coreos/etcd/releases/download/v3.2.25/etcd-v3.2.25-linux-amd64.tar.gz | tar xz
ENV PATH $PATH:/etcd-v3.2.25-linux-amd64

ENV TERM=linux TERMINFO=/etc/terminfo LANG=en_US.UTF-8

USER proxy
ENV HOME=/tmp
COPY mitm_http/mitm_http.py /mitm/
ENTRYPOINT ["mitmdump", "-p", "8080", "-s", "/mitm/mitm_http.py", "--mode", "transparent", "--quiet"]
