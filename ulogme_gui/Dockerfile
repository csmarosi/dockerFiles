FROM debian

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        git vim ca-certificates \
        xdotool xinput \
        python chromium \
    && \
    apt-get clean

RUN git clone https://github.com/csmarosi/ulogme.git

WORKDIR /ulogme
RUN cp render/render_settings_example.js render/render_settings.js && \
    chown 1000 . -R

CMD ["bash"]
