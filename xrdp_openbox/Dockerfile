FROM xrdp_base

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        openbox \
        x11-xserver-utils xloadimage \
        x11-xkb-utils xkb-data \
        ratpoison- \
    && \
    apt-get clean

COPY xrdp_xmonad/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
