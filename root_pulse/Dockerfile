FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        pulseaudio alsa-utils alsa-tools \
    && \
    apt-get clean

COPY root_pulse/setupHacks.sh /root/

EXPOSE 4713
CMD ["/root/setupHacks.sh"]
