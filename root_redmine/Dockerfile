FROM debian:jessie

RUN apt-get update && \
    apt-get install --no-install-recommends -yq \
        mysql-client libapache2-mod-passenger apache2 \
        git openssh-client vim \
        cron \
    && \
    apt-get clean

#Use debconf-get-selections | grep mysql-server to derive these
RUN \
echo mysql-server-5.5 mysql-server/root_password_again password p | debconf-set-selections && \
echo mysql-server-5.5 mysql-server/root_password password p | debconf-set-selections && \
apt-get install --no-install-recommends -yq mysql-server

RUN /etc/init.d/mysql start && \
echo redmine redmine/instances/default/dbconfig-install boolean true | debconf-set-selections && \
echo redmine redmine/instances/default/database-type select mysql | debconf-set-selections && \
echo redmine redmine/instances/default/mysql/admin-pass password p | debconf-set-selections && \
echo redmine redmine/instances/default/mysql/app-pass password | debconf-set-selections && \
apt-get install --no-install-recommends -yq redmine redmine-mysql

RUN ln -s /usr/share/redmine/public/ /var/www/html/redmine && \
    sed -e '/PassengerDefaultRuby/a PassengerDefaultUser www-data' \
        -i /etc/apache2/mods-available/passenger.conf && \
    sed -i /etc/default/cron -e "/EXTRA_OPTS='-l'/s/^# *//" && \
    sed -i /etc/pam.d/cron -e '/pam_loginuid.so/d'

COPY root_redmine/setupHacks.sh /root/
COPY root_redmine/000-default.conf /etc/apache2/sites-available/

ENTRYPOINT ["/root/setupHacks.sh"]
