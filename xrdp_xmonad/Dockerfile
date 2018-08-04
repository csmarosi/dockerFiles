FROM xrdp_base

RUN sed -i /etc/apt/sources.list \
        -e 's! main$! main non-free contrib!'

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        xmobar \
        xmonad libghc-xmonad-contrib-dev \
        x11-xserver-utils xloadimage \
        x11-xkb-utils xkb-data \
        keepassx git openssh-client \
        ratpoison- \
    && \
    apt-get clean

COPY xrdp_xmonad/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
