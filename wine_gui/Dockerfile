FROM debian:sid

RUN dpkg --add-architecture i386 && \
    sed -i /etc/apt/sources.list -e 's!sid main!sid main non-free contrib!'
RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        winetricks wine wine32 fonts-wine \
        libgl1-mesa-dri libgl1-mesa-dri:i386 \
    && \
    apt-get clean

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
