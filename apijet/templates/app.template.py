from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import subprocess
from signal import signal
from signal import SIGKILL
from os import kill
from {project_name}.project import info

# apijet-router-import - auto-generated code do not remove this comment

guinicor_pid=None
origins = ["*"]
app = FastAPI(title=info['name'])
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# apijet-router-include - auto-generated code do not remove this comment


def handler(signal_received, frame):
    kill(guinicor_pid, SIGKILL)
    exit(0)

def start():
    if info['workers'] > 1:
        signal(SIGKILL, handler)
        command = f"gunicorn -w {{info['workers']}} -b {{info['address']}}:{{info['port']}} {{info['name']}}.app:app"
        guinicor_pid = subprocess.Popen(command.split(), stdout=subprocess.PIPE).pid
    else:
        uvicorn.run(app, host=info['address'], port=info['port'])


if __name__ == "__main__":
    start()
