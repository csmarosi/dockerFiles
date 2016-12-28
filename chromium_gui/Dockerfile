FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        strace \
        chromium pulseaudio \
        python3 \
    && \
    apt-get clean

#optional wireshark
RUN true || (apt-get update && \
    echo wireshark-common	wireshark-common/install-setuid	boolean	false | debconf-set-selections && \
    apt-get install --no-install-recommends -y -q wireshark tshark)

COPY chromium_gui/chromium.py /tmp/
COPY chromium_gui/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
