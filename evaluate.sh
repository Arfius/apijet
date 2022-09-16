#!/bin/bash
pytest -s --html=./output/pytest/test-report.html --self-contained-html
flake8 --format=html --htmldir=./output/flake8