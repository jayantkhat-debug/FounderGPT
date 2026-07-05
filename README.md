# FounderGPT / FounderGPT X

FounderGPT started as a Streamlit startup planning platform. FounderGPT X is the next-generation AI operating system for founders, with a Next.js frontend, FastAPI backend, and NVIDIA Build API integration.

## Live Demo

FounderGPT Streamlit demo:

```text
https://foundergpt.streamlit.app/
```

## FounderGPT X Architecture

- `frontend/`: Next.js 15, React, TypeScript, TailwindCSS, Framer Motion.
- `backend/`: FastAPI, Pydantic, SQLAlchemy-ready structure, NVIDIA Build API client.
- `api/`: API specification notes.
- `database/`: database schema plan.
- `agents/` and `prompts/`: AI agent and prompt strategy.

## FounderGPT X Local Setup

### 1. Backend environment

Create `backend/.env` from the example:

```powershell
Copy-Item backend\.env.example backend\.env
```

Set your NVIDIA Build API key in `backend/.env`:

```text
NVIDIA_API_KEY="your_nvidia_build_api_key"
NVIDIA_BASE_URL="https://integrate.api.nvidia.com/v1"
NVIDIA_MODEL="meta/llama-3.1-70b-instruct"
```

Do not put API keys in frontend files.

### 2. Install backend dependencies

```powershell
python -m pip install -r backend\requirements.txt
```

### 3. Start the backend

```powershell
python -m uvicorn app.main:app --app-dir backend --reload --host 127.0.0.1 --port 8000
```

Health check:

```text
http://127.0.0.1:8000/api/v1/health
```

### 4. Frontend environment

Create `frontend/.env.local` from the example:

```powershell
Copy-Item frontend\.env.example frontend\.env.local
```

For local development, `NEXT_PUBLIC_DEV_API_TOKEN="dev"` is accepted by the backend only when `APP_ENV="development"`.

### 5. Install frontend dependencies

```powershell
cd frontend
npm.cmd install
```

### 6. Start the frontend

```powershell
npm.cmd run dev
```

Open:

```text
http://localhost:3000
```

## Chat Endpoint

`POST /api/v1/chat/startup-idea`

Headers:

```text
Authorization: Bearer dev
Content-Type: application/json
```

Body:

```json
{
  "startup_idea": "An AI operating system that helps founders go from idea to funded startup.",
  "conversation_history": []
}
```

Response:

```json
{
  "agent": "FounderGPT X",
  "response": "AI co-founder response..."
}
```

## Verification

Useful checks:

```powershell
python -m compileall backend\app
cd frontend
npm.cmd run typecheck
npm.cmd run build
```

## Author

Jayant Khatri
