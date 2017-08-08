FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        tinyproxy \
    && \
    apt-get clean


COPY tinyproxy/tinyproxy.conf /etc/
USER proxy
ENTRYPOINT ["tinyproxy", "-d", "-c", "/etc/tinyproxy.conf"]
