Based on Debian stable.
It pulls xrdp and X11rdp (the fast X11 backend) directly from github and builds it.
To save space, much of the build data is removed (2G->600M).

Login: `username:password` is `root:p`
Contains only `rxvt` terminal emulator with the `ratpoison` window manager.
To install packages, passwordless sudo is set up as well.

To start it, issue:

    docker run -t -P xrdp_base

Check the listening (ephemeral) port with `docker ps` and run e.g.

    rdesktop -u root -p p 127.0.0.1:32769

Use `Ctrl+t` `c` to open a terminal emulator.

Possible uses:
* base image for app containers (i.e. Firefox, scientific apps)
* documentation on how to build xrdp
* proof-of-concept that this is possible
