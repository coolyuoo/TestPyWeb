# ClassHello

A simple FastAPI project with hello endpoints.

## Features

- Root endpoint with optional name parameter
- Path endpoint for greeting specific names
- FastAPI framework with automatic API documentation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/coolyuoo/ClassHello.git
cd ClassHello
```

2. Create and activate a virtual environment (recommended)

Windows (PowerShell):
```powershell
# create
python -m venv .venv
# activate
.\.venv\Scripts\Activate.ps1
```

Windows (cmd.exe):
```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

Run the application using the venv's Python or uvicorn directly. Replace `main:app` with your ASGI module if different.

PowerShell (activated venv):
```powershell
uvicorn main:app --reload
```

Without activating the venv (explicit python):
```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Root endpoint with optional `name` query parameter
- `GET /hello/{name}` - Greet a specific name

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`