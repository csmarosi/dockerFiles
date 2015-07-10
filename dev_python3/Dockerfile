FROM python

RUN apt-get update -y -q
RUN apt-get install -y -q time
RUN apt-get clean

RUN pip3 install tweepy pykka pytest-quickcheck pyflakes pep8 coverage
