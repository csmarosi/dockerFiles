FROM ubuntu

RUN apt-get update && \
    apt-get install --no-install-recommends -yq \
        strace \
        chromium-browser pulseaudio \
        python3 iputils-ping \
    && \
    apt-get clean

COPY chromium_gui/chromium.py /tmp/
COPY chromium_gui/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
