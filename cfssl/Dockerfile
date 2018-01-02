FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        curl ca-certificates \
        opensc pcscd yubico-piv-tool \
        sudo \
    && \
    apt-get clean

#From https://coreos.com/os/docs/latest/generate-self-signed-certificates.html
RUN mkdir -p /cfssl/bin && \
    curl -L -o /cfssl/bin/cfssl https://pkg.cfssl.org/R1.2/cfssl_linux-amd64 && \
    curl -L -o /cfssl/bin/cfssljson https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64

RUN chmod +x  /cfssl/bin/cfssljson && \
    chmod +sx /cfssl/bin/cfssl

RUN echo 'ALL ALL=NOPASSWD:ALL' > /etc/sudoers.d/allSudo

CMD ["bash"]
