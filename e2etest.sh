pip install ./dist/apiJet-0.0.1-py3-none-any.whl --force-reinstall
export OLDPWD=$(pwd)
cd ~/Downloads
apijet create --port 1234 --name my_project --address 0.0.0.0
cd my_project
apijet endpoint --add my_endpoint
cd -
