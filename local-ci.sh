#! /bin/bash

black --check --line-length 79 src \
&& pycodestyle src \
&& pydocstyle src
coverage run -m pytest tests --html=report.html --self-contained-html
coverage report -m
coverage json
coverage html
