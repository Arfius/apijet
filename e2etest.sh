pip install ./dist/apiJet-0.0.1-py3-none-any.whl --force-reinstall
export OLDPWD=$(pwd)
cd ~/Downloads
apijet create --port 1234 --name test_project --address 0.0.0.0 --database 0.0.0.0
cd test_project
apijet endpoint --add test_endpoint
cd -
