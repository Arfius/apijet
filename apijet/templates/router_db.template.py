from typing import List
from urllib import response
from fastapi import APIRouter, HTTPException, Depends
from {project_name}.models.{import_name} import {endpoint_name}BaseDB, {endpoint_name}FullDB
from {project_name}.core.{import_name} import {endpoint_name}Core
from {project_name}.models.message_db import MessageDB


{endpoint_name}_router = APIRouter()


@{endpoint_name}_router.get('/{endpoint_name}_get_all', response_model=List[{endpoint_name}FullDB], tags=['{endpoint_name}'])
async def get():
    try:
        return {endpoint_name}Core.get_all()
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e)) 


@{endpoint_name}_router.post('/{endpoint_name}_save', tags=['{endpoint_name}'], response_model=MessageDB)
async def get(data:{endpoint_name}BaseDB):
    try:
        return {endpoint_name}Core.save_one(data)
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e)) 


@{endpoint_name}_router.get('/{endpoint_name}_get_one/{{pid}}', tags=['{endpoint_name}'], response_model={endpoint_name}FullDB)
async def get(pid: str):
    try:
        return {endpoint_name}Core.get_one(pid)
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))

@{endpoint_name}_router.patch('/{endpoint_name}_update/{{pid}}', tags=['{endpoint_name}'], response_model=MessageDB)
async def update(pid: str, data: {endpoint_name}BaseDB):
    try:
        return {endpoint_name}Core.update_one(pid, data)
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e)) 


@{endpoint_name}_router.delete('/{endpoint_name}_delete', tags=['{endpoint_name}'], response_model=MessageDB)
async def delete(pid: str):
    try:
        return {endpoint_name}Core.delete_one(pid)
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e)) 