FROM debian:jessie

RUN apt-get update && \
    apt-get install --no-install-recommends -yq \
        apache2 drraw openssh-client \
        vim \
        openssh-server git \
        libapache2-mod-php5 php5-curl \
    && \
    apt-get clean

COPY root_drraw/site.conf /etc/apache2/sites-enabled/
RUN a2enmod cgi

RUN mkdir -p /var/www/collectd && \
    chmod 777 /var/www/collectd && \
    mkdir /var/www/cgi-bin && \
    ln -s /usr/lib/cgi-bin/drraw /var/www/cgi-bin/drraw

COPY root_drraw/*.sh /root/
ENTRYPOINT ["/root/setupHacks.sh"]
