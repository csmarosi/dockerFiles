FROM xrdp_base

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        strace \
        chromium pulseaudio \
    && \
    apt-get clean

COPY chromium_gui/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
