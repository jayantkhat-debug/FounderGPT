# FounderGPT X

FounderGPT X is the AI Operating System for Founders. It helps founders move from idea to funded startup with AI-guided validation, planning, execution, and fundraising workflows.

Build. Validate. Launch. Fund.

From idea to funded startup. AI-powered. Founder-first.

## Introduction

FounderGPT X is designed as a premium founder operating system, not another chatbot. The product combines a Next.js application, FastAPI backend, structured founder memory, and NVIDIA Build API-powered AI guidance to help entrepreneurs pressure-test ideas, understand markets, generate investor-ready assets, and build disciplined startup execution.

## Features

- AI startup idea validation
- Founder-first strategic chat
- Critical assumption testing
- Project and memory-ready backend architecture
- Business plan, pitch deck, market research, and fundraising roadmap foundations
- Modular AI agent system for CEO, CTO, Product, VC, Marketing, Sales, Finance, Legal, Growth, Operations, UX, and Engineering roles
- Secure server-side NVIDIA Build API integration
- Premium dark-mode interface inspired by Apple, Linear, Vercel, and OpenAI

## Architecture

FounderGPT X is organized as a production-ready monorepo with clear separation of concerns:

### Directory Structure
- `frontend/`: Next.js 15, React, TypeScript, TailwindCSS, Framer Motion
- `backend/`: FastAPI, Pydantic, SQLAlchemy-ready domain structure, NVIDIA Build API client
- `database/`: PostgreSQL schema documentation and migration scripts (alembic)
- `api/`: API specifications and route contracts
- `agents/`: AI agent registry and role definitions
- `prompts/`: System prompts and agent strategies
- `docs/`: Architecture, planning, and audit documentation
- `scripts/`: Automation and maintenance utilities

### Note on Legacy Code
Legacy Streamlit files have been archived in `archive/legacy-streamlit/` for reference. The production application uses the new FastAPI backend and Next.js frontend exclusively.

## Tech Stack

- Frontend: Next.js 15, React, TypeScript, TailwindCSS, Framer Motion
- Backend: FastAPI, Python, Pydantic
- Database: PostgreSQL
- ORM: SQLAlchemy
- Authentication: Clerk-ready architecture
- AI: NVIDIA Build API through an OpenAI-compatible client
- Styling: Premium dark mode, glass surfaces, responsive layouts

## Installation

Create the backend environment file:

```powershell
Copy-Item backend\.env.example backend\.env
```

Set your NVIDIA Build API key in `backend/.env`:

```text
NVIDIA_API_KEY="your_nvidia_build_api_key"
NVIDIA_BASE_URL="https://integrate.api.nvidia.com/v1"
NVIDIA_MODEL="meta/llama-3.1-70b-instruct"
```

Install backend dependencies:

```powershell
python -m pip install -r backend\requirements.txt
```

Install frontend dependencies:

```powershell
cd frontend
npm.cmd install
```

## Quick Start

Start the FastAPI backend:

```powershell
cd "C:\Users\91797\OneDrive\FounderGPT V5"
python -m uvicorn app.main:app --app-dir backend --reload --host 127.0.0.1 --port 8000
```

Start the Next.js frontend in a second terminal:

```powershell
cd "C:\Users\91797\OneDrive\FounderGPT V5\frontend"
npm.cmd run dev
```

Open:

```text
http://localhost:3000
```

Health check:

```text
http://127.0.0.1:8000/api/v1/health
```

## Roadmap

- Phase 1: Authentication, dashboard, projects, AI chat, memory, NVIDIA integration
- Phase 2: Business plan generator, pitch deck generator, market research, competitor analysis, financial models
- Phase 3: Investor CRM, task management, calendar, notifications, founder memory
- Phase 4: Multi-agent collaboration, voice, documents, image generation, code generation

## Contributing

FounderGPT X is early and moving quickly. Contributions should preserve production-ready architecture, strict typing, secure secret handling, modular boundaries, and premium product quality.

Before opening a pull request:

```powershell
python -m compileall backend\app
cd frontend
npm.cmd run typecheck
npm.cmd run build
```

## License

Copyright (c) 2026 FounderGPT X.

All Rights Reserved.

## Screenshots

Screenshots will be added as FounderGPT X product surfaces stabilize.

Recommended screenshot filenames:

- `foundergpt-x-dashboard.png`
- `foundergpt-x-chat.png`
- `foundergpt-x-projects.png`

## Future Vision

FounderGPT X should become the world's best AI co-founder: a system that challenges founders, identifies weak assumptions, converts ideas into execution plans, and helps people build fundable companies with discipline and speed.
