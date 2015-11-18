FROM debian:sid

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        file git make \
        fonts-liberation ghostscript imagemagick \
        libreoffice hunspell-en-us \
        pandoc \
        latex-beamer texlive-latex-extra \
        texlive-fonts-extra texlive-fonts-recommended lmodern \
    && \
    apt-get clean

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
