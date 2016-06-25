FROM python

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        time \
        sudo \
    && \
    apt-get clean

RUN pip3 install \
        pytest-quickcheck pyflakes pep8 coverage \
        tweepy pykka \
        ipython matplotlib numpy \
        yapf

RUN echo 'ALL ALL=NOPASSWD:ALL' > /etc/sudoers.d/allSudo

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
