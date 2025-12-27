#! /bin/bash

black --check --line-length 79 src \
&& pycodestyle src \
&& pydocstyle src
coverage run -m pytest tests 
coverage report -m
coverage json
coverage html
