#!/bin/bash
pip list --format=freeze > requirements.txt
#!/bin/bash
VERSION=$(python apijet/version.py)
echo "Creating build for verison $VERSION"
python -m build --outdir ./output/$VERSION
