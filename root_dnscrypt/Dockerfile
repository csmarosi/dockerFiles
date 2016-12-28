FROM debian:sid

RUN apt-get update && \
    apt-get install --no-install-recommends --force-yes -y -q \
        dnscrypt-proxy \
        dnsutils \
        dnsmasq \
    && \
    apt-get clean

COPY root_dnscrypt/setupHacks.sh /
COPY root_dnscrypt/dnsmasq.conf /etc/
ENTRYPOINT ["/setupHacks.sh"]
CMD ["d0wn-us-ns2", "fvz-anytwo"]
