FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        lighttpd \
        debmirror \
        patch ed \
    && \
    apt-get clean

RUN echo 'deb http://172.17.42.1/debian jessie main' > /etc/apt/sources.list

CMD ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
