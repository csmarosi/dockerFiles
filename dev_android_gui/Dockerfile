FROM debian

RUN dpkg --add-architecture i386
RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        libstdc++6:i386 libc6:i386 zlib1g:i386 \
        openjdk-7-jdk ant \
        git x11-apps file strace \
        libgl1-mesa-dri \
        sudo procps \
        python curl zip make schedtool bc \
        abootimg cpio \
        eclipse \
    && \
    apt-get clean

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
