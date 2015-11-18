FROM jess/chrome

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        strace \
        pulseaudio \
    && \
    apt-get clean

COPY chromium_random_gui/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
