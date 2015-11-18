FROM ubuntu:14.04

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        strace \
        chromium-browser pulseaudio \
    && \
    apt-get clean

COPY chromium_random_gui/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
