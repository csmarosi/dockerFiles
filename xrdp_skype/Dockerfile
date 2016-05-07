FROM xrdp_base

#Stolen from @jess:
#https://github.com/jfrazelle/dockerfiles/blob/master/skype/Dockerfile

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    wget http://download.skype.com/linux/skype-debian_4.3.0.37-1_i386.deb && \
    dpkg --force-depends -i skype*.deb && \
    apt-get install -fy
