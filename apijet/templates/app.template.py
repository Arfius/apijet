from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import subprocess
from {project_name}.project import info
import os
import signal
from sys import exit

# apijet-router-import - auto-generated code do not remove this comment

guinicor_pid=None
origins = ["*"]
app = FastAPI(title=info['name'], version=info['version'])
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# apijet-router-include - auto-generated code do not remove this comment

def start():
    if info['workers'] > 1:
        command = f"gunicorn -k uvicorn.workers.UvicornWorker -w {{info['workers']}} -b {{info['address']}}:{{info['port']}} {{info['name']}}.app:app"
        subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        while True:
            pass

    else:
        uvicorn.run(app, host=info['address'], port=info['port'])


if __name__ == "__main__":
    start()
