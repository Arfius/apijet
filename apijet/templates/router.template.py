from fastapi import APIRouter, HTTPException
from {project_name}.models.{import_name} import {endpoint_name}Base
from {project_name}.core.{import_name} import {endpoint_name}Core


{endpoint_name}_router = APIRouter()


@{endpoint_name}_router.post('/{endpoint_name}_reverse', tags=['{endpoint_name}'])
async def reverse(data:{endpoint_name}Base):
    try:
        return {endpoint_name}Core.reverse(data)
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e)) 
