FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        chromium pulseaudio \
        python3 \
    && \
    apt-get clean

#optional wireshark
RUN true || (apt-get update && \
    apt-get install --no-install-recommends -y -q \
        strace gdb \
        sudo \
        wireshark tshark && \
    echo 'ALL ALL=NOPASSWD:ALL' > /etc/sudoers.d/allSudo)

COPY chromium_gui/chromium.py /tmp/
COPY chromium_gui/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
