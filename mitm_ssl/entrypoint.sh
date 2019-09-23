#!/bin/bash
set -euxo pipefail

if [ -n "${PDF_PORT:-}" ]; then
    python3 /mitm/serve_pdf.py &
fi
mitmdump -p 8080 -s /mitm/mitm_ssl.py --quiet
