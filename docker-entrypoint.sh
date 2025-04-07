#!/bin/sh

chown -R nonroot:nonroot database
gosu nonroot gunicorn bytezo_website.main:app -w 4 -b 0.0.0.0:8000