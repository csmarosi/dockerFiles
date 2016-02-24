FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        openssh-server git vim \
        cron \
    && \
    apt-get clean

RUN sed -i /etc/ssh/sshd_config -e 's/^UsePAM.*/UsePAM no/' && \
    sed -i /etc/default/cron -e "/EXTRA_OPTS='-l'/s/^# *//"

COPY root_git/setupHacks.sh /root/
ENTRYPOINT ["/root/setupHacks.sh"]
