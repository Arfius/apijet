#!/bin/bash
VERSION=$(python apijet/version.py)
echo "Evauating verison $VERSION"
pytest -s --html=./output/$VERSION/pytest/test-report.html --self-contained-html
flake8 --format=html --htmldir=./output/$VERSION/flake8