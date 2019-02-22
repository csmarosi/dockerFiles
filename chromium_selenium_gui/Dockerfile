FROM debian:sid

RUN apt-get update && \
    apt-get install --no-install-recommends -yq \
        strace \
        chromium pulseaudio \
        python3 \
        chromium-driver python3-selenium scala \
        curl unzip \
        rxvt-unicode-lite procps x11-apps vim \
        python3-requests openssh-client openjdk-8-jdk \
        sudo \
    && \
    apt-get clean

RUN echo 'ALL ALL=NOPASSWD:ALL' > /etc/sudoers.d/allSudo \
    && echo 'root:p' | chpasswd

RUN mkdir /opt/selenium-java && cd /opt/selenium-java && \
    curl https://selenium-release.storage.googleapis.com/3.1/selenium-java-3.1.0.zip -o /tmp/x.zip && \
    unzip /tmp/x.zip && rm /tmp/x.zip && \
    chmod 755 -Rc .
RUN curl https://downloads.typesafe.com/scalaide-pack/4.7.0-vfinal-oxygen-212-20170929/scala-SDK-4.7.0-vfinal-2.12-linux.gtk.x86_64.tar.gz | tar -zx -C /opt/
RUN mkdir /opt/gradle && \
    curl https://downloads.gradle.org/distributions/gradle-4.6-bin.zip -o /tmp/x.zip && \
    unzip -d /opt/gradle /tmp/x.zip && rm /tmp/x.zip

RUN apt-get remove -yq scala-library scala && \
    curl https://www.scala-lang.org/files/archive/scala-2.11.8.deb -o /tmp/s.deb && \
    dpkg -i /tmp/s.deb && rm /tmp/s.deb

#optional wireshark
RUN true || (apt-get update && \
    apt-get install --no-install-recommends -yq wireshark tshark)

COPY chromium_gui/chromium.py /tmp/
COPY chromium_gui/entrypoint.sh /

ENTRYPOINT ["/bin/bash"]
