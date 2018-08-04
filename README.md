# dockerFiles
This repo contains the definitions of my containers.
I use them to keep my main system clean.

There are elaborate hacks here, so most probably you don't want to clone the whole repo;
you might find some of them useful though.
The scripts in the bin/ directory are in my PATH, while the others are not.

Some containers are less hacky, some even contain their own README files.

## SUDO workaround/hack
In current (i.e., after stretch) Debian sid, sudo does not work when `/etc/shadow`
 is not bind-mounted (i.e., only `/etc/passwd` is there). Typing `sudo -i` gives:

    sudo: account validation failure, is your account locked?

Workaround is to issue:

    su -c "echo $(whoami):$(whoami) | chpasswd"

This means, that the images here (may) have the root password set to `p`.

## License
MIT
