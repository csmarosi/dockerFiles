FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        openssh-server git vim \
    && \
    apt-get clean

RUN sed -i /etc/ssh/sshd_config -e 's/^UsePAM.*/UsePAM no/'

COPY root_git/setupHacks.sh /root/
ENTRYPOINT ["/root/setupHacks.sh"]
