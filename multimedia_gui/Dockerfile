FROM debian:sid

RUN sed -i /etc/apt/sources.list \
        -e 's! main$! main non-free contrib!' \
        -e '$a deb http://www.deb-multimedia.org/ sid main non-free'

RUN apt-get update && \
    apt-get install --force-yes -yq deb-multimedia-keyring && \
    apt-get install --no-install-recommends --force-yes -y -q \
        pulseaudio mplayer \
        vlc \
        mc wget \
        sxiv \
        ffmpeg \
        python3 \
        libid3-tools \
    && \
    apt-get clean

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
