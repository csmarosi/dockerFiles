# Introduction
A containerized version of [ulogme](https://github.com/karpathy/ulogme) (with Docker-patches).
Contains built-in Chromium because the container should not have network.
Check (in)security section too!

## Usage
To start recording your computer usage, run something like:

    docker run -it -d --net=none -u=$(id -u) -e HOME=/ulogme -e DISPLAY=:0 -v /tmp/.X11-unix/X0:/tmp/.X11-unix/X0:ro -v /etc/passwd:/etc/passwd:ro ulogme_gui /ulogme/ulogme.sh

To check the report, `docker exec` into the container, and run:

    python ulogme_serve.py &
    python export_events.py
    chromium --no-sandbox http://localhost:8124

With this configuration, all the logs are inside the container; they will be lost when the container is removed.
Bind mount (-v) the /ulogme from a permanent place to prevent this.


# (In)Security
Altough the container does not have network (`--net=none`), it is just a little bit harder to leak all your data.
The ulogme script cannot directly connect to the internet, but knows all about you including your sudo password.
In theory it could wait until you are away, type something in, and boom, similar to
[How to turn your KVM into a raging key-logging monster](https://media.ccc.de/v/32c3-7189-key-logger_video_mouse#video)
