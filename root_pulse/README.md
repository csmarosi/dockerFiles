A containerized pulseaudio server.
I do not want to plug cables into my netbook, and this lets me play audio over the wifi.
To start it, run something like:
    docker run -d -p 4713:4713 -v /dev/snd:/dev/snd --privileged root_pulse
