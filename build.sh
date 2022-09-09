#!/bin/bash
python -m pip freeze > requirements.txt
python setup.py bdist_wheel