FROM debian:sid

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        strace \
        chromium pulseaudio \
        python3 \
        chromium-driver python3-selenium \
        scala \
    && \
    apt-get clean

#http://selenium-release.storage.googleapis.com/3.1/selenium-java-3.1.0.zip
RUN apt-get install --no-install-recommends -y -q \
        unzip \
        rxvt-unicode-lite procps \
        python3-requests openssh-client \
        sudo \
    && \
    echo 'ALL ALL=NOPASSWD:ALL' > /etc/sudoers.d/allSudo

#optional wireshark
RUN true || (apt-get update && \
    apt-get install --no-install-recommends -y -q wireshark tshark)

COPY chromium_gui/chromium.py /tmp/
COPY chromium_gui/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
