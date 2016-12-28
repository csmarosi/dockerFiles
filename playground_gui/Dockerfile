FROM debian:sid

RUN dpkg --add-architecture i386 && \
    sed -i /etc/apt/sources.list -e 's!sid main!sid main non-free contrib!'

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        sudo gitk openssh-client make vim file \
        g++ gdb valgrind strace \
        julia \
        python3-dev ipython3-qtconsole \
        r-base r-cran-ggplot2 r-cran-rjson r-cran-reshape2 \
    && \
    apt-get clean

RUN echo 'ALL ALL=NOPASSWD:ALL' > /etc/sudoers.d/allSudo

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
