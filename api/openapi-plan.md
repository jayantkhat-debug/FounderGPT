# FounderGPT X API Specification

FounderGPT X — The AI Operating System for Founders.

Base path: `/api/v1`

Authentication: `Authorization: Bearer <clerk_jwt>` for every protected route.

## Health

### GET `/health`

Returns service status and version.

## Projects

### GET `/projects`

Returns projects owned by the authenticated user.

### POST `/projects`

Creates a startup project.

Request:

```json
{
  "startup_name": "FounderGPT X",
  "idea": "AI operating system for founders",
  "target_users": "First-time and repeat startup founders",
  "market": "Startup tooling",
  "revenue_model": "Subscription",
  "funding_stage": "Pre-seed"
}
```

### GET `/projects/{project_id}`

Returns one project with core memory summary.

### PATCH `/projects/{project_id}`

Updates project profile fields.

## Conversations

### GET `/projects/{project_id}/conversations`

Lists project conversations.

### POST `/projects/{project_id}/conversations`

Creates a conversation.

## AI Chat

### POST `/chat/startup-idea`

Evaluates a founder's startup idea using FounderGPT X and NVIDIA Build API.

Request:

```json
{
  "startup_idea": "An AI operating system that helps founders go from idea to funded startup.",
  "conversation_history": [
    {
      "role": "user",
      "content": "I want to build this for first-time founders."
    },
    {
      "role": "assistant",
      "content": "Who is the narrowest initial user?"
    }
  ]
}
```

Response:

```json
{
  "agent": "FounderGPT X",
  "response": "Critical, actionable startup advice from the AI co-founder."
}
```

### POST `/projects/{project_id}/chat`

Sends a message to a selected agent.

Request:

```json
{
  "conversation_id": "uuid",
  "agent_key": "ceo",
  "message": "Should I build this idea?",
  "workflow": "business_validation"
}
```

Response:

```json
{
  "message_id": "uuid",
  "agent_key": "ceo",
  "content": "Actionable, critical founder guidance.",
  "follow_up_questions": [],
  "memory_updates": [],
  "suggested_tasks": []
}
```

## Agents

### GET `/agents`

Returns available AI agents with key, name, specialty, and personality summary.

## Documents

### POST `/projects/{project_id}/documents/generate`

Generates a structured artifact such as business plan, pitch deck outline, market research, or YC application draft.

## Tasks

### GET `/projects/{project_id}/tasks`

Lists tasks.

### POST `/projects/{project_id}/tasks`

Creates a task.

## Error Shape

```json
{
  "error": {
    "code": "validation_error",
    "message": "Human-readable message",
    "request_id": "uuid"
  }
}
```
