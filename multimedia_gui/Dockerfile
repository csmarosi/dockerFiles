FROM debian:sid

RUN sed -i /etc/apt/sources.list \
        -e 's! main$! main non-free contrib!' \
        -e '$a deb http://www.deb-multimedia.org/ sid main non-free'

RUN apt-get -oAcquire::AllowInsecureRepositories=true update && \
    apt-get -oAcquire::AllowInsecureRepositories=true \
        install --allow-unauthenticated -yq deb-multimedia-keyring && \
    apt-get install --no-install-recommends -yq --allow-unauthenticated \
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
