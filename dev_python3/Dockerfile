FROM python

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        time \
    && \
    apt-get clean

RUN pip3 install tweepy pykka pytest-quickcheck pyflakes pep8 coverage
