<div align="center">
  <img src="apijet.png" width="360" />
</div>

<div align="center">
  ⚙ <strong>A command line tool to deploy python Rest APIS in 20 secs.</strong> ⚙
</div>
<br/>

<p align="center">
  
  <a target="_blank" rel="noopener noreferrer" href="https://github.com/Arfius/apijet/actions/workflows/test.yml/badge.svg">
    <img src="https://github.com/Arfius/apijet/actions/workflows/test.yml/badge.svg" alt="ci/cd" style="max-width: 100%;"/>
  </a>

  <a target="_blank"  href="https://twitter.com/alfarruggia">
    <img src="https://img.shields.io/twitter/follow/alfarruggia"/>
  </a>
</p>

<p align="center">
  <br/>
  <a style="{text-decoration: none;} " target="_blank"  href="https://medium.com/p/de089348c498"> 🔗 Example of a backend for a TODO app </a>
</p>

---

Apijet is a Python framework for building APIs via the command line. Apijet is a useful framework for fast prototyping Rest APIs. Apijet will deploy python code according to the well-defined pattern [(see here)](#pattern), you only have to pay attention to the business logic and to the database queries. 

You will be able to deploy endpoints following these 5 steps:

1. **Install apijet**
Once you have installed the package, __apijet__ will be available as bash command.
```
$> pip install apijet
```
2. **Create a project**
The __create__ command generates the skeleton of the project and the main project files.
```
$> apijet create --name myProject --port 9090 --address 127.0.0.1
$> cd my_projet
```
3. **Add and endpoint.**
The endpoint can also need database support, in this case, you pass the **--database** parameter and Apijet will generate the code for **CRUD** basic operation for the endpoint. If you need database support, you make sure that __mongodb__ is running. Consider a Docker container to deploy an instance in a short time [(see here)](#mongodb-container).
```
$> apijet endpoint --name myEndpoint
```
4. **Run the server**
```
$> python -m my_projet.app
```
5. **Open your browser**
The APIs will be exposed according the automatic interactive API documentation by [Swagger](https://swagger.io/).
Open your browser @ http://127.0.0.1:9090/docs to test out your work!


These steps generate a follow folder and file structure:
```
.
|-- myProject
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
The project configuration is saved in the _apijet.json_ file:
``` json
{
    "name": "myProject",
    "port": 1234,
    "address": "127.0.0.1",
    "workers": 1,
    "mongo": {
        "auth": false,
        "address": "127.0.0.1",
        "port": 27017,
        "username": "",
        "password": ""
    },
    "endpoints": [
        "myEndpoint"
    ]
}
```
where:
  - __address__ and __port__  are used by the web server.
  - if __workers__ > 1, __Gunicorn__ will be started otherwise __Unicorn__ as ASGI web server
  - if __mongo.auth__ is true, __mongo.username__ and __mongo.password__ are requested

<div id="mongodb-container" ></div>
#### Run MongoDB in a docker contaienr
If you are a fan of docker and you want to run an instance of MongoDb without stress:
```$> docker run -d -p 27017:27017 --name myProject-db mongo:latest```

<div id="pattern" ></div>

## Source code and pattern.

Apijet project folder contains the auto-generated python code. The code is arranged in four folders: core, repository, router and models. When a new endpoint is added, a new file in each of these four folders is created. These four files have the same name (_/myEndpoint.py_) of the endpoint but they have different behaviour, see the following pattern.

<div align="center">
  <img src="pattern.png" width="440" />
</div>

#### Router 
Files created as routers expose the endpoints, they receive the user request and send back the response. (_i.e. router/myEndpoint.py_)

#### Core
Files as core implement the business logic. Your algorithms and data processing stuff go here. (_i.e. core/myEndpoint.py_)

#### Repository
Files as repositories make the interaction with the database. Your queries go here. (_i.e. repository/myEndpoint.py_)

#### Models
For each endpoint, core, repository, and router communicate through the data structure. The data structure is located in the folder models. You modify this file with the parameters you need to handle in your project.


<p align="center">
 <br/>
   <a style="{text-decoration: none;} " target="_blank"  href="https://medium.com/p/de089348c498"> 🔗 Follow this link for the example on how to implement a backend for a TODO app </a>
</p>

---
## Expose an endpoint in 20 secs.

![Alt Text](example.gif)

---
## Dev-Stack

The code is generated exploiting the following development stack :

- **MongoDB** : Document database - [🔗](https://www.mongodb.com/)

- **Pymongo** : Python library for working with MongoDB - [🔗](https://pymongo.readthedocs.io/en/stable/)

- **FastApi** : RestApi framework -[🔗](https://fastapi.tiangolo.com/)

- **Pydantic** : Python data validator & more - [🔗](https://pydantic-docs.helpmanual.io/)

- **Uvicorn** : ASGI web server implementation for Python - [🔗](https://www.uvicorn.org/)

## CLI Commands

#### Helper
```
$> apijet -h
usage: apijet [-h] {create,endpoint,remove} ...

apijet - Api Generator v: 0.2.2

optional arguments:
  -h, --help            show this help message and exit

Actions:
  {create,endpoint,remove}
    create              Create a new project
    endpoint            Add or Remove an endpointto the project
    remove              Remove a project
```

#### Create a projet
```
$> apijet create -h
usage: apijet create [-h] [--port PORT] [--name NAME] [--address ADDRESS]

optional arguments:
  -h, --help         show this help message and exit
  --port PORT        port where apis are exposed
  --name NAME        project name
  --address ADDRESS  ip address where apis are exposed
```

#### Add an endpoint
```
$> apijet endpoint -h
usage: apijet endpoint [-h] [--add ADD] [--database] [--remove REMOVE]

optional arguments:
  -h, --help       show this help message and exit
  --add ADD        endpoint name
  --database       say that the endpoint needs database support
  --remove REMOVE  not supported yet
  
```