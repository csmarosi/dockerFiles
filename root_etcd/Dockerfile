FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        curl \
        git vim \
        ca-certificates \
    && \
    apt-get clean

RUN curl -L  https://github.com/coreos/etcd/releases/download/v2.2.2/etcd-v2.2.2-linux-amd64.tar.gz -o etcd-v2.2.2-linux-amd64.tar.gz && \
    tar xzvf etcd-v2.2.2-linux-amd64.tar.gz && \
    echo DONE

ENV PATH $PATH:/etcd-v2.2.2-linux-amd64

CMD ["/magic/start.sh"]
