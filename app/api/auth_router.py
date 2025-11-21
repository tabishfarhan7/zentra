from fastapi import APIRouter, Depends
from sqlalchemy.orm import session

from app.db.database import get_db #type: ignore
from app.schemas.auth import Token, UserCreate, UserLogin, UserResponse #type: ignore
from app.services.auth_service import create_user, authenticate_user
from app.core.dependencies import get_current_user
from app.db import models #type: ignore


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/signup",response_model=UserResponse)
def signup(user_data: UserCreate, db:session = Depends(get_db)): # type: ignore
    new_user=create_user(db, user_data) # type: ignore
    return new_user # type: ignore
    
    
@router.post("/login",response_model=Token)
def login(user_data: UserLogin, db:session = Depends(get_db)): # type: ignore
    token=authenticate_user(db, user_data) # type: ignore
    return token # type: ignore

@router.get("/me")
def read_current_user(current_user: models.User = Depends(get_current_user)): 
    return {
        "id": current_user.id,
        "email": current_user.email
    }