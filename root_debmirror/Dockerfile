FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        lighttpd \
        debmirror \
        patch ed xz-utils \
    && \
    apt-get clean

CMD ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
