FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        curl ca-certificates \
    && \
    apt-get clean

#From https://coreos.com/os/docs/latest/generate-self-signed-certificates.html
RUN mkdir -p /cfssl/bin && \
    curl -L -o /cfssl/bin/cfssl https://pkg.cfssl.org/R1.1/cfssl_linux-amd64 && \
    curl -L -o /cfssl/bin/cfssljson https://pkg.cfssl.org/R1.1/cfssljson_linux-amd64

RUN chmod +x  /cfssl/bin/cfssljson && \
    chmod +sx /cfssl/bin/cfssl

CMD ["bash"]
