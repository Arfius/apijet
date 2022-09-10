from fastapi import APIRouter, HTTPException, Depends
from {project_name}.models.{endpoint_name} import {endpoint_name}Out, {endpoint_name}In
from {project_name}.core.{endpoint_name} import get_all, save_one, get_one


{endpoint_name}_router = APIRouter()


@{endpoint_name}_router.get('/{endpoint_name}_get_all', response_model=List[{endpoint_name}Out], tags=['{endpoint_name}'])
async def get():
    try:
        return  get_all()
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e)) 


@{endpoint_name}_router.post('/{endpoint_name}_save', tags=['{endpoint_name}'])
async def get():
    try:
        return save_one()
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e)) 


@{endpoint_name}_router.post('/{endpoint_name}_get_one/{{pid}}', tags=['{endpoint_name}'])
async def get(pid: str):
    try:
        return get_one(pid)
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e)) 