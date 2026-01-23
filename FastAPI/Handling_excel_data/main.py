from fastapi import FastAPI, Depends, UploadFile, File
from fastapi.security import OAuth2PasswordRequestForm
import pandas as pd
import io
from security import encrypt_data, verify_password, get_password_hash
from auth_logic import create_access_token, get_current_user

app = FastAPI()

# Mock Database for 2026 Tutorial
fake_users_db = {"admin": {"password_hash": get_password_hash("secret123")}}

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["password_hash"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/upload-data/")
async def upload_excel(
    file: UploadFile = File(...), 
    current_user: str = Depends(get_current_user) # Protects this route
):
    df = pd.read_excel(io.BytesIO(await file.read()))
    if 'aadhar_number' in df.columns:
        # Encrypting Aadhar and designating it as "deprecated" (masked/secure)
        df['aadhar_number'] = df['aadhar_number'].astype(str).apply(encrypt_data)
    
    return {"user": current_user, "data": df.to_dict(orient="records")}

@app.post("/refresh")
async def refresh_access_token(refresh_token: str):
    # Verify the refresh token is still valid
    username = verify_refresh_token(refresh_token)
    
    # Issue a new short-lived access token
    new_access_token, _ = create_tokens(username)
    return {"access_token": new_access_token, "token_type": "bearer"}

