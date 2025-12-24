from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.db import models #type: ignore
from app.schemas.auth import UserCreate, UserLogin #type: ignore
from app.core.security import hash_password, verify_password, create_access_token #type: ignore


# -------------------------------------
# 1) CREATE USER (SIGNUP)
# -------------------------------------
def create_user(db: Session, user_data: UserCreate):
    # check if user already exists
    existing = db.query(models.User).filter(models.User.email == user_data.email).first() # type: ignore
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    # hash the password
    hashed_pw = hash_password(user_data.password)

    # create user object
    new_user = models.User(
        email=user_data.email,
        hashed_password=hashed_pw,
    )

    # save to DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# -------------------------------------
# 2) LOGIN USER
# -------------------------------------
def authenticate_user(db: Session, user_data):
    # find user - username field contains the email for OAuth2PasswordRequestForm
    email = user_data.username if hasattr(user_data, 'username') else user_data.email
    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid email or password",
        )

    # verify password
    if not verify_password(user_data.password, user.hashed_password): #type: ignore
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # create JWT token
    token = create_access_token({"sub": user.email})

    return {"access_token": token, "token_type": "bearer"}
