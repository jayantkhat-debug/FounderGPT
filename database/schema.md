# FounderGPT X Database Schema

PostgreSQL is the source of truth for founder memory, project state, conversations, documents, and planning artifacts.

## Tables

### users

- `id`: UUID primary key
- `clerk_user_id`: unique text
- `email`: text
- `full_name`: text nullable
- `created_at`: timestamptz
- `updated_at`: timestamptz

### projects

- `id`: UUID primary key
- `owner_id`: UUID foreign key to `users.id`
- `startup_name`: text
- `idea`: text
- `target_users`: text nullable
- `market`: text nullable
- `competitors`: jsonb default `[]`
- `revenue_model`: text nullable
- `funding_stage`: text nullable
- `status`: enum draft, validating, building, fundraising, scaling, archived
- `health_score`: integer nullable
- `created_at`: timestamptz
- `updated_at`: timestamptz

### conversations

- `id`: UUID primary key
- `project_id`: UUID foreign key to `projects.id`
- `title`: text
- `created_at`: timestamptz
- `updated_at`: timestamptz

### messages

- `id`: UUID primary key
- `conversation_id`: UUID foreign key to `conversations.id`
- `agent_key`: text nullable
- `role`: enum system, user, assistant, tool
- `content`: text
- `metadata`: jsonb default `{}`
- `created_at`: timestamptz

### memories

- `id`: UUID primary key
- `project_id`: UUID foreign key to `projects.id`
- `kind`: enum startup_profile, customer, market, competitor, revenue, goal, roadmap, risk, insight
- `content`: jsonb
- `confidence`: numeric
- `source_message_id`: UUID nullable
- `created_at`: timestamptz
- `updated_at`: timestamptz

### documents

- `id`: UUID primary key
- `project_id`: UUID foreign key to `projects.id`
- `kind`: enum business_plan, pitch_deck, market_research, yc_application, financial_model, markdown, json
- `title`: text
- `content`: jsonb
- `export_status`: enum draft, queued, exported, failed
- `created_at`: timestamptz
- `updated_at`: timestamptz

### tasks

- `id`: UUID primary key
- `project_id`: UUID foreign key to `projects.id`
- `title`: text
- `description`: text nullable
- `priority`: enum low, medium, high, critical
- `status`: enum todo, doing, blocked, done
- `due_date`: date nullable
- `created_at`: timestamptz
- `updated_at`: timestamptz

### roadmaps

- `id`: UUID primary key
- `project_id`: UUID foreign key to `projects.id`
- `horizon`: enum daily, weekly, monthly, quarterly
- `title`: text
- `items`: jsonb
- `created_at`: timestamptz
- `updated_at`: timestamptz

## Indexes

- `users.clerk_user_id`
- `projects.owner_id`
- `conversations.project_id`
- `messages.conversation_id, messages.created_at`
- `memories.project_id, memories.kind`
- `documents.project_id, documents.kind`
- `tasks.project_id, tasks.status`

## Data Principles

- Conversation history is append-only.
- Memory is editable and confidence-scored.
- Generated documents store structured JSON first; PDF, Word, PowerPoint, Markdown, and JSON exports are views over stored content.
- User-owned project data is always scoped by authenticated owner.
