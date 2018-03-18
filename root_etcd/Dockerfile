FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        curl \
        git vim \
        ca-certificates \
    && \
    apt-get clean

RUN curl -L https://github.com/coreos/etcd/releases/download/v3.2.17/etcd-v3.2.17-linux-amd64.tar.gz | tar xz

ENV PATH $PATH:/etcd-v3.2.17-linux-amd64

CMD ["/magic/start.sh"]
