import secrets
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, Request, status
# from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from backend.endpoints import add_user, get_password, get_userid
from backend.schemas import Token, User

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    try:
        if len(hashed_password) == 0 or hashed_password is None:
            print("Verification false")
            return False
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        print("Error occured at verify password : ",e)
        return False


def create_access_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    to_encode.update( {"iat": datetime.utcnow()})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def is_token_expired(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        expiration_time = datetime.fromtimestamp(payload["exp"])
        current_time = datetime.utcnow()
        return current_time > expiration_time
    except JWTError:
        # Invalid token format or signature
        return True

def check_user(request: Request):
    token = request.headers.get("Authorization")
    print(token)
    if not token or is_token_expired(token):
        return 401
    return 200

@router.post("/auth/register", response_model=Token)
async def register(request: Request, user: User):
    try:
        incomming = await request.json()
        user_id = secrets.token_hex(8)
        username = incomming['username']
        hashed_password = get_password_hash(incomming['password'])
        email_id = incomming['email']
        await add_user(user_id, username, hashed_password, email_id)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user_id}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        ) from error

@router.post("/auth/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    stored_hashed_password = await get_password(username)
    print(stored_hashed_password)
    if stored_hashed_password is None or not verify_password(password, stored_hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    user_id = await get_userid(username)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
