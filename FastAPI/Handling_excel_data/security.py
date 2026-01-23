from cryptography.fernet import Fernet
from passlib.context import CryptContext

# Encryption Setup
ENCRYPTION_KEY = Fernet.generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)

# Hashing Setup (Best Practice: Use Argon2 or Bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def encrypt_data(data: str) -> str:
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data: str) -> str:
    return cipher_suite.decrypt(encrypted_data.encode()).decode()

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
