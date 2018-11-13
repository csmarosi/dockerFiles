FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -yq \
        openssh-server git vim \
        cron gpg \
    && \
    apt-get clean

RUN sed -i /etc/ssh/sshd_config -e 's/^UsePAM.*/UsePAM no/' && \
    sed -i /etc/default/cron -e "/EXTRA_OPTS='-l'/s/^# *//" && \
    sed -i /etc/pam.d/cron -e '/pam_loginuid.so/d'

COPY root_git/setupHacks.sh /root/
ENTRYPOINT ["/root/setupHacks.sh"]
