const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000/api/v1";

export type Agent = {
  key: string;
  name: string;
  specialty: string;
  personality: string;
};

export type ChatResponse = {
  message_id: string | null;
  agent_key: string;
  content: string;
  follow_up_questions: string[];
  memory_updates: Record<string, unknown>[];
  suggested_tasks: Record<string, unknown>[];
};

type RequestOptions = {
  token: string;
  body?: unknown;
};

export async function apiRequest<T>(path: string, options: RequestOptions): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    method: options.body ? "POST" : "GET",
    headers: {
      Authorization: `Bearer ${options.token}`,
      "Content-Type": "application/json",
    },
    body: options.body ? JSON.stringify(options.body) : undefined,
    cache: "no-store",
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(text || `Request failed with ${response.status}`);
  }

  return response.json() as Promise<T>;
}
