FROM debian:sid

RUN apt-get update && \
    apt-get install --no-install-recommends --force-yes -y -q \
        dnscrypt-proxy \
        dnsutils \
    && \
    apt-get clean

ENTRYPOINT ["/usr/sbin/dnscrypt-proxy"]
CMD ["-a", "0.0.0.0:5353", "-R", "fvz-rec-at-vie-01"]
