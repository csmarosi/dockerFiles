FROM debian:jessie

RUN dpkg --add-architecture i386
RUN apt-get update && \
    apt-get install --no-install-recommends -yq \
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

ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_HOME}/tools
#android list sdk --extended
RUN cd /opt && \
    VERSION=android-sdk_r24-linux.tgz && \
    curl http://dl.google.com/android/$VERSION -o $VERSION && \
    tar xzf $VERSION && \
    echo y > accept.txt && \
    android update sdk --no-ui --filter platform-tools-preview < accept.txt && \
    android update sdk --no-ui --filter build-tools-23.0.1 < accept.txt && \
    android update sdk --no-ui --filter android-16 < accept.txt && \
    android update sdk --no-ui --filter android-19 < accept.txt && \
    android update sdk --no-ui --filter android-23 < accept.txt

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
