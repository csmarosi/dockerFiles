FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -yq \
        qemu \
        bochs-x \
        git git-svn vim \
        sudo usbutils \
        procps curl \
    && \
    apt-get clean

RUN echo 'ALL ALL=NOPASSWD:ALL' > /etc/sudoers.d/allSudo \
    && echo 'root:p' | chpasswd

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
