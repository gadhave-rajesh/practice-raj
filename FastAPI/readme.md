To create a complete beginner-friendly guide, save the following content as FASTAPI_SETUP.md. This includes the prerequisites, installation steps for 2025, and the testing instructions.
markdown

# FastAPI Beginner's Guide 
Below is git resource with working demos

**Cookbook PDF :**
http://103.203.175.90:81/fdScript/RootOfEBooks/E%20Book%20collection%20-%202025%20-%20D/CSE%20%20IT%20AIDS%20ML/Packt.FastAPI.Cookbook.pdf

**Git resources:**
https://github.com/PacktPublishing/FastAPI-Cookbook


This pre-requistites guide covers everything from setting up your environment to testing your first API.

## 1. Prerequisites
Before starting, ensure you have the following installed on your system:
* **Python 3.12+**: Download from [python.org](www.python.org).
* **VS Code**: Recommended editor for FastAPI development.

---

## 2. Environment Setup & Installation
It is best practice to use a virtual environment to keep your dependencies organized.

### Step A: Create Project Folder
```cmd
mkdir my_fastapi_app
cd my_fastapi_app
Use code with caution.
```

### Step B: Create & Activate Virtual Environment
```cmd
Windows:
cmd
python -m venv venv
venv\Scripts\activate
Use code with caution.
```

```cmd
Mac / Linux:
bash
python3 -m venv venv
source venv/bin/activate
```
Use code with caution.

### Step C: Install Required Packages
In 2025, the [standard] tag is the recommended way to install FastAPI and its server (Uvicorn) together.
cmd
pip install "fastapi[standard]"
Use code with caution.

## 3. How to Run the Server
Once your code (e.g., main.py) is ready, start the server using the FastAPI CLI:
cmd
fastapi dev main.py
Use code with caution.

The server will typically start at http://127.0.0.1:8000.

## 4. Testing the API
cmd
- Method 1: Interactive Web Docs (Recommended)
    Open Docs: Go to 127.0.0.1.
    Select Endpoint: Click the POST /items route.
    Try it out: Click the "Try it out" button.
    Input Data: Enter a string (e.g., "Apple") in the request body.
    Execute: Click the blue "Execute" button to see the result.

cmd
- Method 2: Terminal (curl)
  Open a new terminal window while the server is running.
  Windows (cmd):
  cmd
  curl -X POST "127.0.0.1" -H "Content-Type: application/json" -d "\"My Item\""
  Use code with caution.

cmd
Mac / Linux (bash):
bash
curl -X POST "127.0.0.1" \
     -H "Content-Type: application/json" \
     -d '"My Item"'
Use code with caution.

5. Summary of curl Flags
cmd
  Flag	Name	Purpose
  -X POST	Method	Tells the server you want to "Create/Send" data.
  -H	Header	Informs the server that the data is in JSON format.
  -d	Data	The actual content you are sending to the API.

7. Verify Results
Check the current list of items at any time by visiting:
127.0.0.1
{content: }
