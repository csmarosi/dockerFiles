FROM debian:sid

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        mysql-client ca-certificates \
        git openssh-client vim \
        cron apache2 \
    && \
    apt-get clean

RUN \
echo mysql-server-5.5 mysql-server/root_password_again password p | debconf-set-selections && \
echo mysql-server-5.5 mysql-server/root_password password p | debconf-set-selections && \
apt-get install --no-install-recommends -q -y mysql-server

RUN /etc/init.d/mysql start && \
echo tt-rss tt-rss/dbconfig-install boolean true | debconf-set-selections && \
echo tt-rss tt-rss/database-type select mysql | debconf-set-selections && \
echo tt-rss tt-rss/mysql/app-pass password | debconf-set-selections && \
echo tt-rss tt-rss/mysql/admin-pass password p | debconf-set-selections && \
echo tt-rss tt-rss/reconfigure-webserver multiselect apache2 | debconf-set-selections && \
echo tt-rss tt-rss/self_url_path string 127.0.0.1/tt-rss | debconf-set-selections && \
apt-get install --no-install-recommends -q -y tt-rss

RUN sed -i /etc/default/tt-rss -e 's/DISABLED=1/DISABLED=0/' && \
    sed -i /etc/tt-rss/config.php -e 's!http://example.org!http://127.0.0.1!' && \
    sed -i /etc/mysql/mysql.conf.d/mysqld.cnf \
        -e '/^\[mysqld\]$/a innodb_flush_log_at_trx_commit = 2' && \
    ln -s /usr/share/tt-rss/www/ /var/www/html/tt-rss && \
    sed -i /etc/default/cron -e "/EXTRA_OPTS='-l'/s/^# *//" && \
    sed -i /etc/pam.d/cron -e '/pam_loginuid.so/d'

COPY root_ttrss/setupHacks.sh /root/
ENTRYPOINT ["/root/setupHacks.sh"]
