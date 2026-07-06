const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

export type Agent = {
  key: string;
  name: string;
  specialty: string;
  personality: string;
};

export type ChatResponse = {
  message_id: string | null;
  conversation_id: string | null;
  agent_key: string;
  content: string;
  follow_up_questions: string[];
  memory_updates: Record<string, unknown>[];
  suggested_tasks: Record<string, unknown>[];
};

export type ConversationMessage = {
  role: "user" | "assistant";
  content: string;
};

export type StartupIdeaChatResponse = {
  agent: string;
  response: string;
};

export type Project = {
  id: string;
  name: string;
  description: string;
  stage: string;
  created_at: string;
  updated_at: string;
};

export type ProjectMemory = {
  id: string;
  project_id: string;
  startup_name: string | null;
  problem: string | null;
  solution: string | null;
  customer: string | null;
  revenue_model: string | null;
  pricing: string | null;
  competitors: Record<string, unknown>[];
  goals: Record<string, unknown>[];
};

export type Conversation = {
  id: string;
  project_id: string;
  title: string;
  created_at: string;
  updated_at: string;
};

export type PersistedMessage = {
  id: string;
  conversation_id: string;
  agent_key: string | null;
  role: "system" | "user" | "assistant" | "tool";
  content: string;
  created_at: string;
};

type RequestOptions = {
  token: string;
  method?: "GET" | "POST" | "PATCH" | "PUT" | "DELETE";
  body?: unknown;
};

export async function apiRequest<T>(path: string, options: RequestOptions): Promise<T> {
  if (!API_BASE_URL) {
    throw new Error("NEXT_PUBLIC_API_BASE_URL is not configured.");
  }

  const response = await fetch(`${API_BASE_URL}${path}`, {
    method: options.method ?? (options.body ? "POST" : "GET"),
    headers: {
      Authorization: `Bearer ${options.token}`,
      "Content-Type": "application/json",
    },
    body: options.body ? JSON.stringify(options.body) : undefined,
    cache: "no-store",
  });

  if (!response.ok) {
    let message = `Request failed with ${response.status}`;
    try {
      const data = (await response.clone().json()) as { detail?: string | { msg?: string }[] };
      if (typeof data.detail === "string") {
        message = data.detail;
      } else if (Array.isArray(data.detail) && data.detail[0]?.msg) {
        message = data.detail[0].msg;
      }
    } catch {
      const text = await response.text();
      message = text || message;
    }
    throw new Error(message);
  }

  if (response.status === 204) {
    return undefined as T;
  }

  return response.json() as Promise<T>;
}

export async function evaluateStartupIdea(input: {
  startupIdea: string;
  conversationHistory: ConversationMessage[];
  token?: string;
}) {
  return apiRequest<StartupIdeaChatResponse>("/chat/startup-idea", {
    token: input.token ?? process.env.NEXT_PUBLIC_DEV_API_TOKEN ?? "dev",
    body: {
      startup_idea: input.startupIdea,
      conversation_history: input.conversationHistory,
    },
  });
}

export async function listProjects(token = process.env.NEXT_PUBLIC_DEV_API_TOKEN ?? "dev") {
  return apiRequest<Project[]>("/projects", { token });
}

export async function createProject(
  input: { name: string; description: string; stage: string },
  token = process.env.NEXT_PUBLIC_DEV_API_TOKEN ?? "dev",
) {
  return apiRequest<Project>("/projects", {
    token,
    body: input,
  });
}

export async function getProjectMemory(projectId: string, token = process.env.NEXT_PUBLIC_DEV_API_TOKEN ?? "dev") {
  return apiRequest<ProjectMemory>(`/projects/${projectId}/memory`, { token });
}

export async function listConversations(projectId: string, token = process.env.NEXT_PUBLIC_DEV_API_TOKEN ?? "dev") {
  return apiRequest<Conversation[]>(`/projects/${projectId}/conversations`, { token });
}

export async function listMessages(
  projectId: string,
  conversationId: string,
  token = process.env.NEXT_PUBLIC_DEV_API_TOKEN ?? "dev",
) {
  return apiRequest<PersistedMessage[]>(`/projects/${projectId}/conversations/${conversationId}/messages`, { token });
}

export async function generateBusinessModel(
  projectId: string,
  token = process.env.NEXT_PUBLIC_DEV_API_TOKEN ?? "dev",
) {
  return apiRequest<{ business_model: string }>(`/projects/${projectId}/generate-business-model`, {
    token,
    method: "POST",
  });
}

export async function generateWeb3Strategy(
  projectId: string,
  token = process.env.NEXT_PUBLIC_DEV_API_TOKEN ?? "dev",
) {
  return apiRequest<{ web3_strategy: string }>(`/projects/${projectId}/generate-web3-strategy`, {
    token,
    method: "POST",
  });
}

export async function generateBusinessPlan(
  projectId: string,
  token = process.env.NEXT_PUBLIC_DEV_API_TOKEN ?? "dev",
) {
  return apiRequest<{ business_plan: string }>(`/projects/${projectId}/generate-business-plan`, {
    token,
    method: "POST",
  });
}

export async function generateFinancialModel(
  projectId: string,
  token = process.env.NEXT_PUBLIC_DEV_API_TOKEN ?? "dev",
) {
  return apiRequest<{ financial_model: string }>(`/projects/${projectId}/generate-financial-model`, {
    token,
    method: "POST",
  });
}
