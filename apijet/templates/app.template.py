from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# apijet-router-import - auto-generated code do not remove this comment

origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# apijet-router-include - auto-generated code do not remove this comment


def start():
    uvicorn.run(app, host="{address}", port={port})


if __name__ == "__main__":
    start()
