# Create and use endpoint 

-- To build a modular FastAPI application that securely handles Excel data, you can use Pandas for data processing and Cryptography (Fernet) for encryption. 
-- Following 2026 industry standards, sensitive identifiers like Aadhar numbers must be stored in encrypted format to prevent unauthorized exposure.


# 🚀 FastAPI Secure Excel Processor (2026 Edition)

A modular, production-ready FastAPI application designed to securely process Excel data. 
This project follows **2026 Industry Best Practices** by implementing **Fernet Encryption** for sensitive identifiers (Aadhar numbers), **Bcrypt Hashing** for passwords, and **OAuth2 with JWT Refresh Tokens**.

---

## 📂 Project Structure

```text
project/
├── main.py          # FastAPI application & API endpoints
├── security.py      # Fernet Encryption & Bcrypt Hashing logic
├── auth_logic.py    # JWT Generation & Refresh Token logic
├── client.py        # Python script to authenticate and fetch/decrypt data
├── requirements.txt # Project dependencies
└── data.xlsx        # Sample Excel file (Required columns: name, aadhar_number)

1. Create a Virtual Environment (venv)
Isolate your project dependencies to ensure a clean environment.
Windows:
  bash
    python -m venv venv
    venv\Scripts\activate

2. Install Required Libraries
  bash
    pip install fastapi uvicorn pandas openpyxl cryptography requests python-multipart python-jose[cryptography] passlib[bcrypt]


🚀 Execution Steps
Step 1: Start the API Server
Run the FastAPI server using Uvicorn.
  bash
    uvicorn main:app --reload

  - Interactive API Docs: Visit 127.0.0.1 to test the endpoints.

Step 2: Run the Client Script
Open a new terminal tab, activate your venv, and run the script to authenticate and process the Excel file.
  bash
    python client.py


🔒 Security Implementation
1. Aadhar Encryption (Data at Rest & Transit)
Standard: Uses Cryptography.io Fernet (Symmetric encryption).
Process: The aadhar_number column is encrypted immediately upon upload. The API response contains only the encrypted strings, ensuring sensitive data is never exposed in plain text.
2. Password Hashing
Standard: Passwords are never stored in plain text.
Implementation: Uses Bcrypt via passlib. Verification is performed by comparing the provided password against the stored secure hash.
3. OAuth2 with Refresh Tokens
Access Token: Valid for 15 minutes. Used for every API request.
Refresh Token: Valid for 7 days. Used to automatically generate a new Access Token without requiring the user to re-login.
Safety: Tokens are signed using the HS256 algorithm to prevent tampering.
🛠️ Modular Design Explained
security.py: Handles mathematical security (encryption/decryption/hashing).
auth_logic.py: Manages identity and session security (JWT creation/validation).
main.py: Handles business logic (Excel processing) and API routing.
client.py: A standalone script demonstrating how a frontend or another service would securely consume this API.
📝 Requirements Checklist
Python 3.10+
An Excel file named data.xlsx with a column header aadhar_number.
Note: In production, always store SECRET_KEY and ENCRYPTION_KEY in a .env file rather than code.




