FROM debian:sid

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install --no-install-recommends -y -q \
        okular \
        kcachegrind graphviz \
    && \
    apt-get clean
