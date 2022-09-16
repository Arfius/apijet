#!/bin/bash
pip list --format=freeze > requirements.txt
python setup.py bdist_wheel --dist-dir ./output
python setup.py clean --all