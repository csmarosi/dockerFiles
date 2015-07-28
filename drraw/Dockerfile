FROM debian

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install --no-install-recommends -y -q \
        apache2 drraw sudo openssh-client \
        vim \
    && \
    apt-get clean

COPY allSudo /etc/sudoers.d/
COPY site.conf /etc/apache2/sites-enabled/
RUN a2enmod cgi

RUN mkdir -p /var/www/collectd && \
    chmod 777 /var/www/collectd && \
    mkdir /var/www/cgi-bin && \
    ln -s /usr/lib/cgi-bin/drraw /var/www/cgi-bin/drraw
