FROM debian:sid

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install --no-install-recommends -y -q \
        file \
        texlive-fonts-recommended texlive-latex-extra lmodern \
        pandoc libreoffice \
        imagemagick \
    && \
    apt-get clean

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
