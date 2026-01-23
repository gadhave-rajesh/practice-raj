import requests
from security import decrypt_data

API_URL = "http://127.0.0.1:8000"

def secure_fetch(file_path):
    # 1. Authenticate to get JWT Token
    login_data = {"username": "admin", "password": "secret123"}
    token_res = requests.post(f"{API_URL}/token", data=login_data)
    token = token_res.json()["access_token"]
    
    # 2. Upload with Bearer Token
    headers = {"Authorization": f"Bearer {token}"}
    with open(file_path, 'rb') as f:
        response = requests.post(f"{API_URL}/upload-data/", files={'file': f}, headers=headers)
    
    # 3. Read and Decrypt
    data = response.json().get("data", [])
    for row in data:
        decrypted = decrypt_data(row['aadhar_number'])
        print(f"User: {row.get('name')}, Aadhar: {decrypted}")


def fetch_data_with_retry(file_path, access_token, refresh_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    with open(file_path, 'rb') as f:
        response = requests.post(f"{API_URL}/upload-data/", files={'file': f}, headers=headers)
    
    # If Access Token expired, use Refresh Token to get a new one
    if response.status_code == 401:
        print("Access token expired. Refreshing...")
        refresh_res = requests.post(f"{API_URL}/refresh", params={"refresh_token": refresh_token})
        new_token = refresh_res.json()["access_token"]
        
        # Retry original request with NEW access token
        headers = {"Authorization": f"Bearer {new_token}"}
        # (Re-open file and retry logic here)


if __name__ == "__main__":
    secure_fetch("data.xlsx")

