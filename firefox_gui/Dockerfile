FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -yq \
        firefox-esr pulseaudio \
        python3 \
    && \
    apt-get clean

ENTRYPOINT ["/usr/bin/firefox"]
