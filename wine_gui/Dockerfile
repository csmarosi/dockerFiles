FROM debian:sid

RUN dpkg --add-architecture i386 && \
    sed -i /etc/apt/sources.list -e 's!sid main!sid main non-free contrib!'
RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install --no-install-recommends -y -q \
        winetricks wine wine32 fonts-wine \
    && \
    apt-get clean
