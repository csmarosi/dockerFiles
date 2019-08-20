FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -yq \
        file git make \
        fonts-liberation ghostscript imagemagick \
        libreoffice hunspell-en-us \
        pandoc \
        texlive-latex-recommended texlive-latex-extra \
        texlive-fonts-extra texlive-fonts-recommended lmodern \
        sxiv gpaint tesseract-ocr \
        okular \
        kcachegrind graphviz \
    && \
    apt-get clean

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
