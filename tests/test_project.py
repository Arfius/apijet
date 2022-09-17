from time import sleep
from apijet.commands.create import create
from apijet.commands.remove import remove
from apijet.commands.endpoint import add
import subprocess
import os
import pytest
from signal import SIGKILL
from os import kill
import requests


@pytest.fixture
def run_project():
    print("🧪> Run server")
    os.chdir('./test_project')
    bashCommand = "python test_project/app.py"
    pid = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE).pid
    print('🧪> wait 5 seconds to warm up the server...')
    sleep(5)
    yield
    kill(pid, SIGKILL)
    print(f'🧪> Process {pid} killed')
    os.chdir('../')


def test_create_projet_with_endpoint():
    assert create('test_project', 1234, '127.0.0.1', './') is True
    assert add('test_endpoint', './test_project', False) is True
    assert add('test_endpoint_db', './test_project', True) is True


def test_get_info_project():
    os.chdir('./test_project')
    from test_project.test_project.project import info
    assert info['port'] == 1234
    assert info['name'] == 'test_project'
    assert info['address'] == '127.0.0.1'
    os.chdir('../')


def test_reverse_endpoint(run_project):
    from test_project.test_project.models.test_endpoint import test_endpointBase
    message = "hello world"
    t_e = test_endpointBase(text=message)
    x = requests.post('http://127.0.0.1:1234/test_endpoint_reverse', json=t_e.dict())
    assert x.status_code == 200
    assert x.json()['text'] == message[::-1]


def test_reverse_endpoint_db(run_project):
    x = requests.get('http://127.0.0.1:1234/test_endpoint_db_get_all')
    assert x.status_code == 200


def test_remove_project():
    assert remove('./test_project') is True
