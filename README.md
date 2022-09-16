<div align="center">
  <img src="apijet.png" width="360" />
</div>

<div align="center">
  ⚙ <strong>A command line tool to deploy python RestApi in 20 secs.</strong> ⚙
</div>
<br/>

<p align="center">
  <a target="_blank" rel="noopener noreferrer" href="https://github.com/Arfius/apijet/actions/workflows/apijet.yml/badge.svg">
    <img src="https://github.com/Arfius/apijet/actions/workflows/apijet.yml/badge.svg" alt="ci/cd" style="max-width: 100%;"/>
  </a>

  <a target="_blank"  href="https://twitter.com/alfarruggia">
    <img src="https://img.shields.io/twitter/follow/alfarruggia"/>
  </a>
 </p>
 <p align="center">
 
   <a style="{text-decoration: none;} " target="_blank"  href="https://medium.com/p/de089348c498"> 🔗 how to use </a>

</p>

---

Apijet is python framework for building APIs via command line.

Apijet generates python code following the below pattern.

<table style="{border:0px}">
<tr>
	<td>
		<img src="pattern.png" width="360" />
	</td>
	<td> 
		<h5> Router </h5> Expose the Endpoints. Receive the user request.
		<h5> Core </h5> Implement the bussines logic.
		<h5> Repository </h5> Database interaction layer.
	</td>
</tr>
<table>

---
## Expose an endpoint in 20 secs.

![Alt Text](example.gif)

---
## Technologies

The code is created exploiting  the following development stack :

- **MongoDB** : Document database - [🔗](https://www.mongodb.com/)

```
# How to run a mongodb instance via docker container
$> docker run -d -p 27017:27017 --name my-mongo mongo:latest

``` 

- **Pymongo** : Python library for working with MongoDB - [🔗](https://pymongo.readthedocs.io/en/stable/)

- **FastApi** : RestApi framework -[🔗](https://fastapi.tiangolo.com/)

- **Pydantic** : Python data validator & more - [🔗](https://pydantic-docs.helpmanual.io/)

- **Uvicorn** : ASGI web server implementation for Python - [🔗](https://www.uvicorn.org/)

## CLI Commands


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
$> ls 
.
|-- myApi
|   |-- core
|   |-- database
|   |   |-- dbmanager.py
|   |   |-- message.py
|   |   `-- pyobjectid.py
|   |-- models
|   |-- routers
|   `-- app.py
`-- apijet.json
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
$> ls 
.
|-- myApi
|   |-- core
|   |   |
|   |   `-- myEndpoint.py
|   |-- database
|   |   |-- dbmanager.py
|   |   |-- message.py
|   |   |-- myEndpoint.py
|   |   `-- pyobjectid.py
|   |-- models
|   |   |
|   |   `-- myEndpoint.py
|   |-- routers
|   |   |
|   |   `-- myEndpoint.py
|   `-- app.py
`-- apijet.json
```
### Deploy

```
$> python myApi/app.py
INFO:     Started server process [40471]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:1234 (Press CTRL+C to quit)
```
To get access to the interactive-api-docs follow this [link](https://fastapi.tiangolo.com/#interactive-api-docs), for example @ http://0.0.0.0:1234/docs