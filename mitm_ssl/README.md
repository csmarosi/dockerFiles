# Introduction
A (man in the middle) web proxy that modifies pages. It will strip away HTTPS.

Example uses:
* no TLS negotiation: make HTTPS-only sites work with very old browsers again
* spare bandwidth for mobile: strip away media content (feature-flag)
* strip annoying noscript/refresh tags: view 'normal' twitter without JavaScript

HTTPS sites can be recognised from the `.ssl` TLD.

## Features flags

Some features are controlled by environment (`-e` in `docker run`):
* `FILTER_CONTENT` for reducing bandwidth (default: on)
* `FORCE_HTTPS` for only viewing HTTPS sited (default: off)
* `PDF_PORT` a port where a python web-server handles Android download manager (requests from a browser-only proxy)

See tests in `tst/run_dockerized_tests.sh` on how to run the containers.
