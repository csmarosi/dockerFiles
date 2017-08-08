FROM debian:jessie

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

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        bison build-essential flex gnupg gperf libesd0-dev liblz4-tool libncurses5-dev libsdl1.2-dev libxml2 libxml2-utils lzop maven pngcrush squashfs-tools xsltproc zlib1g-dev \
        g++-multilib gcc-multilib lib32ncurses5-dev lib32z1-dev \
        make

RUN echo 'ALL ALL=NOPASSWD:ALL' > /etc/sudoers.d/allSudo

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
