#!/bin/bash

python3 app.py &

python3 scraper.py & 

wait -n
  
exit $?