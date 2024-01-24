from fastapi import APIRouter, Depends
from bson.objectid import ObjectId
from app.serializers.userSerializers import userResponseEntity

from app.database import User
from .. import schemas, oauth2

router = APIRouter()


@router.get('/')
def index():
    return {"message": "Welcome to the API DW MTS!"}