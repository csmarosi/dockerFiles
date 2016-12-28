FROM debian:sid

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        firefox \
    && \
    apt-get clean

CMD ["firefox"]
