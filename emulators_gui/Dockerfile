FROM debian:sid

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        freerdp-x11 \
        qemu \
        bochs-x \
        git git-svn vim \
        sudo usbutils \
    && \
    apt-get clean

RUN echo 'ALL ALL=NOPASSWD:ALL' > /etc/sudoers.d/allSudo

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
