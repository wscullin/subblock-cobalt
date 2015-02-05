#!/bin/bash

openssl req -x509 -nodes -days 1000 -batch -newkey rsa:1024 \
  -out ${SC_CONFIGPATH}/cobalt.cert -keyout ${SC_CONFIGPATH}/cobalt.key

