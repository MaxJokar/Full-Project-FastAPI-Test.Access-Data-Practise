from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
import token
from fastapi.security import OAuth2AuthorizationCodeBearer
from blog import token

# to check the Token is valid or not


# where to fectch the Token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.very_token(data, credentials_exception)
