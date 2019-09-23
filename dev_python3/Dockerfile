FROM python

RUN apt-get update && \
    apt-get install --no-install-recommends -yq \
        time \
        sudo \
    && \
    apt-get clean

RUN pip3 install \
        pytest-quickcheck pyflakes pycodestyle coverage \
        tweepy pykka \
        ipython matplotlib numpy \
        scikit-learn \
        yapf

RUN echo 'ALL ALL=NOPASSWD:ALL' > /etc/sudoers.d/allSudo \
    && echo 'root:p' | chpasswd

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
