from fastapi import APIRouter, Response, status, HTTPException, Depends, APIRouter, Form, Query
from typing import List, Optional, Annotated
from ..database import database

router = APIRouter(
    prefix="/articles",
    tags=['Articles']
)

@router.on_event("startup")
async def startup_db_client():
    await database.connect()

@router.on_event("shutdown")
async def shutdown_db_client():
    await database.disconnect()

@router.get("/items/")
async def read_items():
    items = await database.db["articles"].find({'approved': 'yes'}, {'_id': 0}).sort ( { 'created_at' : -1 } ).to_list(100)
    return items