#!/bin/sh 

cd /lib/example/

sudo ntpdate pool.ntp.org
python3 -u widget.py 