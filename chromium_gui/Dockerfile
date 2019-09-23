FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -yq \
        chromium pulseaudio \
        python3 \
    && \
    apt-get clean

#optional wireshark
RUN true || (apt-get update && \
    apt-get install --no-install-recommends -yq \
        strace gdb \
        sudo \
        wireshark tshark && \
    echo 'ALL ALL=NOPASSWD:ALL' > /etc/sudoers.d/allSudo \
    && echo 'root:p' | chpasswd)

COPY chromium_gui/chromium.py /tmp/
COPY chromium_gui/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
