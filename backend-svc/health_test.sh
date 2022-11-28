#!/usr/bin/bash

curl --fail http://127.0.0.1:5000/ip || exit 1

curl --fail http://127.0.0.1:5000/st || exit 1

curl --fail http://127.0.0.1:5000/dns || exit 1
