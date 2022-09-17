from typing import List
from fastapi import APIRouter, HTTPException, Depends
from {project_name}.models.{endpoint_name} import {endpoint_name}BaseDB, {endpoint_name}FullDB
from {project_name}.core.{endpoint_name} import {endpoint_name}Core


{endpoint_name}_router = APIRouter()


@{endpoint_name}_router.get('/{endpoint_name}_get_all', response_model=List[{endpoint_name}FullDB], tags=['{endpoint_name}'])
async def get():
    try:
        return {endpoint_name}Core.get_all()
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e)) 


@{endpoint_name}_router.post('/{endpoint_name}_save', tags=['{endpoint_name}'])
async def get(data:{endpoint_name}BaseDB):
    try:
        return {endpoint_name}Core.save_one(data)
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e)) 


@{endpoint_name}_router.get('/{endpoint_name}_get_one/{{pid}}', tags=['{endpoint_name}'])
async def get(pid: str):
    try:
        return {endpoint_name}Core.get_one(pid)
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))
