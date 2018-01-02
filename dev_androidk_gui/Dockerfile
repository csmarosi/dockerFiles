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
        imagemagick unzip \
        bison build-essential fakeroot flex gperf \
        libalgorithm-diff-xs-perl libalgorithm-merge-perl \
        libfile-fcntllock-perl libxml2-utils \
        lzop \
    && \
    apt-get clean

RUN echo 'ALL ALL=NOPASSWD:ALL' > /etc/sudoers.d/allSudo

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
