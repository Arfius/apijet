# apijet CLI ✈️ 
**A command line tool to deploy python RestApi in few steps.**


![Alt Text](example.gif)

#### Design pattern
Apijet generates the code for each endpoint following below design pattern.

**Core** : Manipulate data. Put here the business logic of your endpoint.

🔃

**Model** : It is the data structure of your endpoint. Edit this file to customise your entity. 

🔃

**Router** : RestApi component that interact with external word. Expose the CRUD endoints for the model.


#### Development stack

**MongoDB** : Document database - [🔗](https://www.mongodb.com/)

**Pymongo** : Python library for working with MongoDB - [🔗](https://pymongo.readthedocs.io/en/stable/)

**FastApi** : RestApi framework -[🔗](https://fastapi.tiangolo.com/)

**Pydantic** : Python data validator & more - [🔗](https://pydantic-docs.helpmanual.io/)

**Uvicorn** : ASGI web server implementation for Python - [🔗](https://www.uvicorn.org/)


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
To get access to the interactive-api-docs follow this [link](https://fastapi.tiangolo.com/#interactive-api-docs)