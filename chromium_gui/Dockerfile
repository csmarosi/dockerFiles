FROM debian:sid

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install --no-install-recommends -y -q \
        strace gdb \
        chromium-dbg pulseaudio \
    && \
    apt-get clean
