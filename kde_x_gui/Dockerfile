FROM debian:sid

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        okular \
        kcachegrind graphviz \
    && \
    apt-get clean

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
