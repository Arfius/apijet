#!/bin/bash
pip list --format=freeze > requirements.txt
#!/bin/bash
VERSION=$(python apijet/version.py)
echo "Creating build for verison $VERSION"
python setup.py bdist_wheel --dist-dir ./output/$VERSION
python setup.py clean --all