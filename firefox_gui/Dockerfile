FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        firefox-esr pulseaudio \
        python3 \
    && \
    apt-get clean

CMD ["firefox"]
