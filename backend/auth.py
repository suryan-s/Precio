import secrets
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from backend.schemas import User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        expiration_time = datetime.fromtimestamp(payload["exp"])
        current_time = datetime.utcnow()
        print("current_time > expiration_time : ", current_time > expiration_time)
        username: str = payload.get("sub")  # type: ignore
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username=username)
    if user is None:
        raise credentials_exception
    return user


def get_user(username: str):
    for user in fake_users_db:
        if user["username"] == username:
            return User(**user)
    return None


def is_token_expired(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        expiration_time = datetime.fromtimestamp(payload["exp"])
        current_time = datetime.utcnow()
        return current_time > expiration_time
    except JWTError:
        # Invalid token format or signature
        return True


fake_users_db = [
    {"username": "suryan", "password": get_password_hash("suryan")},
    {"username": "user", "password": get_password_hash("pass")},
]


@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(username=form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/protected-route")
def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": "You are accessing a protected route!"}


@router.get("/verify-token")
def verify(current_user: User = Depends(get_current_user)):
    return {"message": "Token is valid!"}
