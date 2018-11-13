FROM jess/chrome

USER root

RUN apt-get update && \
    apt-get install --no-install-recommends -yq \
        strace \
        pulseaudio \
        python3 \
    && \
    apt-get clean

COPY chromium_gui/chromium.py /tmp/
COPY chromium_gui/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
