# FounderGPT X Backend API

FastAPI-based backend for FounderGPT X. Designed for deployment on Railway.

## Local Development

### Setup

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Configuration

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Set your NVIDIA Build API key and other required values in `.env`.

### Run Locally

```bash
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Health check: `http://127.0.0.1:8000/api/v1/health`
API docs: `http://127.0.0.1:8000/docs`

## Production Deployment on Railway

### Prerequisites

- PostgreSQL database (Railway PostgreSQL add-on recommended)
- NVIDIA Build API key
- Clerk authentication (optional - can run without)

### Environment Variables

Railway will set these automatically or you must configure:

```
APP_ENV=production
FRONTEND_ORIGINS=https://your-vercel-domain.vercel.app
FRONTEND_ORIGIN=https://your-vercel-domain.vercel.app
DATABASE_URL=postgresql://...  (Railway sets this automatically)
NVIDIA_API_KEY=...
NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1
NVIDIA_MODEL=meta/llama-3.1-70b-instruct
PORT=8000  (Railway sets this automatically)
```

### Deployment

Railway will automatically:
1. Install dependencies from `requirements.txt`
2. Run the `web` command from `Procfile`
3. Expose the service via `https://foundergpt-production.up.railway.app`

The Procfile specifies:
```
web: python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### Health Check

Once deployed:
```
https://foundergpt-production.up.railway.app/api/v1/health
```

Should return: `{"status": "ok", "service": "foundergpt-x-api"}`

## API Routes

### Health
- `GET /api/v1/health` - Service health check

### Chat
- `POST /api/v1/chat/startup-idea` - Evaluate startup idea (requires bearer token)

### Projects (requires authentication)
- `GET /api/v1/projects` - List user projects
- `POST /api/v1/projects` - Create project
- `GET /api/v1/projects/{id}` - Get project

### Agents
- `GET /api/v1/agents` - List available agents

## Architecture

- **Framework**: FastAPI
- **Database**: PostgreSQL + SQLAlchemy ORM
- **Auth**: Clerk JWT tokens
- **AI**: NVIDIA Build API (OpenAI-compatible)
- **Async**: Uvicorn ASGI server with async request handling

## Key Services

- `chat_service.py` - Handles AI responses and chat logic
- `nvidia_client.py` - NVIDIA Build API integration with retry logic
- `project_service.py` - Project and conversation persistence
- `user_service.py` - User management and Clerk integration

## Database Migrations

Alembic migrations are in `alembic/`. To create a new migration:

```bash
alembic revision --autogenerate -m "description"
```

To apply migrations:

```bash
alembic upgrade head
```
