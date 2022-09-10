# apijet CLI ✈️ 
**A command line tool to deploy RestApi in few steps.**

#### What it does
Apijet permits to create a python project and manage RestApi endpoints.

Apijet generates the code for each endpoint following below design pattern:
**Database** ↔️ **Core** ↔️ **Model** ↔️ **Router**

The development stack exploited by apijet is:
**MongoDB** ↔️ **Pymongo** ↔️ **FastApi** ↔️ **Pydantic** ↔️ **Uvicorn/Gunicorn**



### Installation
```
$> pip install -U apijet 
$> apijet -h
usage: apijet [-h] {create,endpoint,remove} ...

apiJet - Api Generator v: 0.1.2

optional arguments:
  -h, --help            show this help message and exit

Actions:
  {create,endpoint,remove}
    create              Create a new project
    endpoint            Add or Remove an endpoint to the project
    remove              Remove a project
```

### Create a projet
```
$> apijet create -h
usage: apijet create [-h] [--port PORT] [--name NAME] [--address ADDRESS]

optional arguments:
  -h, --help         show this help message and exit
  --port PORT        port where apis are exposed
  --name NAME        project name
  --address ADDRESS  ip address where apis are exposed

$> apijet create --name myApi --address 0.0.0.0 --port 1234
$> cd myApi
```

### Add an endpoint
```
$> apijet endpoint -h
usage: apijet create [-h] [--port PORT] [--name NAME] [--address ADDRESS]

optional arguments:
  -h, --help         show this help message and exit
  --port PORT        port where apis are exposed
  --name NAME        project name
  --address ADDRESS  ip address where apis are exposed
(base) alfonsofarruggia@192 prova % apijet endpoint -h
usage: apijet endpoint [-h] [--add ADD] [--remove REMOVE]

optional arguments:
  -h, --help       show this help message and exit
  --add ADD        endpoint name
  --remove REMOVE  endpoint name
  
$> apijet endpoint --add myEndpoint 
```
### Deploy

```
$> python myApi/app.py
INFO:     Started server process [40471]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:1234 (Press CTRL+C to quit)
```
