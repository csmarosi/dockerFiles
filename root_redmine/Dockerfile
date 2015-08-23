FROM debian

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install --no-install-recommends -y -q \
        mysql-client libapache2-mod-passenger apache2 \
        git openssh-client vim \
    && \
    apt-get clean

#Use debconf-get-selections | grep mysql-server to derive these
RUN \
echo mysql-server-5.5 mysql-server/root_password_again password p | debconf-set-selections && \
echo mysql-server-5.5 mysql-server/root_password password p | debconf-set-selections && \
apt-get install --no-install-recommends -q -y mysql-server

RUN /etc/init.d/mysql start && \
echo redmine redmine/instances/default/dbconfig-install boolean true | debconf-set-selections && \
echo redmine redmine/instances/default/database-type select mysql | debconf-set-selections && \
echo redmine redmine/instances/default/mysql/admin-pass password p | debconf-set-selections && \
echo redmine redmine/instances/default/mysql/app-pass password | debconf-set-selections && \
apt-get install --no-install-recommends -q -y redmine redmine-mysql

RUN ln -s /usr/share/redmine/public/ /var/www/html/redmine && \
sed -i '/PassengerDefaultRuby/a PassengerDefaultUser www-data' /etc/apache2/mods-available/passenger.conf

COPY root_redmine/setupHacks.sh /root/
COPY root_redmine/000-default.conf /etc/apache2/sites-available/

ENTRYPOINT ["/root/setupHacks.sh"]
