from datetime import datetime, timedelta, timezone
from jose import jwt
from fastapi import HTTPException

SECRET_KEY = "SUPER_SECRET_KEY"  # Store in environment variables
ALGORITHM = "HS256"

def create_tokens(username: str):
    """Creates both Access and Refresh tokens."""
    # 1. Access Token: Short-lived (15 mins) for API calls
    access_expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    access_token = jwt.encode({"sub": username, "exp": access_expire}, SECRET_KEY, algorithm=ALGORITHM)
    
    # 2. Refresh Token: Long-lived (7 days) only to get new access tokens
    refresh_expire = datetime.now(timezone.utc) + timedelta(days=7)
    refresh_token = jwt.encode({"sub": username, "exp": refresh_expire, "type": "refresh"}, SECRET_KEY, algorithm=ALGORITHM)
    
    return access_token, refresh_token

def verify_refresh_token(token: str):
    """Validates the refresh token and returns the username."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")
        return payload.get("sub")
    except Exception:
        raise HTTPException(status_code=401, detail="Refresh token expired or invalid")
