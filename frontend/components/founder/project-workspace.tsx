"use client";

import { FormEvent, useCallback, useEffect, useState } from "react";
import { useAuth } from "@clerk/nextjs";
import { CalendarDays, FolderKanban, Loader2, Plus } from "lucide-react";

import { Button } from "@/components/ui/button";
import { GlassCard } from "@/components/ui/glass-card";
import { createProject, listProjects, type Project } from "@/lib/api";

const stages = ["Idea", "Validating", "Building", "Fundraising", "Scaling"];

export function ProjectWorkspace() {
  if (process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY) {
    return <ClerkProjectWorkspace />;
  }

  return <ProjectWorkspaceInner tokenMode="development" />;
}

function ClerkProjectWorkspace() {
  const { getToken } = useAuth();
  const resolveClerkToken = useCallback(async () => {
    const token = await getToken();
    if (!token) throw new Error("Missing Clerk session token.");
    return token;
  }, [getToken]);

  return <ProjectWorkspaceInner tokenMode="clerk" getToken={resolveClerkToken} />;
}

function ProjectWorkspaceInner({
  getToken,
  tokenMode,
}: {
  getToken?: () => Promise<string>;
  tokenMode: "clerk" | "development";
}) {
  const [projects, setProjects] = useState<Project[]>([]);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [stage, setStage] = useState(stages[0]);
  const [isLoading, setIsLoading] = useState(true);
  const [isCreating, setIsCreating] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const resolveToken = useCallback(async () => {
    if (getToken) {
      return getToken();
    }

    return process.env.NEXT_PUBLIC_DEV_API_TOKEN ?? "dev";
  }, [getToken]);

  useEffect(() => {
    let active = true;
    resolveToken()
      .then((token) => listProjects(token))
      .then((data) => {
        if (active) setProjects(data);
      })
      .catch((caught) => {
        if (active) setError(caught instanceof Error ? caught.message : "Could not load projects.");
      })
      .finally(() => {
        if (active) setIsLoading(false);
      });
    return () => {
      active = false;
    };
  }, [resolveToken, tokenMode]);

  async function handleCreate(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!name.trim() || !description.trim() || isCreating) return;

    setIsCreating(true);
    setError(null);
    try {
      const token = await resolveToken();
      const project = await createProject({ name: name.trim(), description: description.trim(), stage }, token);
      setProjects((current) => [project, ...current]);
      setName("");
      setDescription("");
      setStage(stages[0]);
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Could not create project.");
    } finally {
      setIsCreating(false);
    }
  }

  return (
    <div className="grid gap-5 xl:grid-cols-[0.85fr_1.15fr]">
      <GlassCard>
        <div className="flex items-center gap-2 text-sm font-medium text-founder-ink">
          <Plus className="h-4 w-4 text-founder-cyan" />
          Create startup
        </div>
        <form onSubmit={handleCreate} className="mt-5 space-y-4">
          <input
            value={name}
            onChange={(event) => setName(event.target.value)}
            placeholder="CPS Research Lab"
            className="h-11 w-full rounded-md border border-border bg-black/30 px-3 text-sm text-founder-ink outline-none placeholder:text-muted focus:border-founder-cyan/45"
          />
          <textarea
            value={description}
            onChange={(event) => setDescription(event.target.value)}
            placeholder="Describe the startup, customer, and current hypothesis."
            className="min-h-28 w-full resize-none rounded-md border border-border bg-black/30 px-3 py-3 text-sm leading-6 text-founder-ink outline-none placeholder:text-muted focus:border-founder-cyan/45"
          />
          <select
            value={stage}
            onChange={(event) => setStage(event.target.value)}
            className="h-11 w-full rounded-md border border-border bg-black/30 px-3 text-sm text-founder-ink outline-none focus:border-founder-cyan/45"
          >
            {stages.map((item) => (
              <option key={item}>{item}</option>
            ))}
          </select>
          <Button type="submit" disabled={!name.trim() || !description.trim() || isCreating} className="w-full gap-2">
            {isCreating ? <Loader2 className="h-4 w-4 animate-spin" /> : <Plus className="h-4 w-4" />}
            Create project
          </Button>
        </form>
        {error ? <p className="mt-4 text-sm leading-6 text-red-100">{error}</p> : null}
      </GlassCard>

      <GlassCard className="p-0">
        <div className="border-b border-border p-5">
          <div className="flex items-center gap-2 text-sm font-medium text-founder-ink">
            <FolderKanban className="h-4 w-4 text-founder-cyan" />
            Projects
          </div>
          <p className="mt-2 text-sm text-muted">Every startup workspace has its own memory and conversation history.</p>
        </div>
        <div className="space-y-3 p-5">
          {isLoading ? (
            <div className="flex items-center gap-2 text-sm text-muted">
              <Loader2 className="h-4 w-4 animate-spin text-founder-cyan" />
              Loading projects...
            </div>
          ) : null}

          {!isLoading && projects.length === 0 ? (
            <div className="rounded-md border border-border bg-black/20 p-5 text-sm leading-6 text-muted">
              No startup projects yet. Create one to start building FounderGPT X memory.
            </div>
          ) : null}

          {projects.map((project) => (
            <div key={project.id} className="rounded-md border border-border bg-black/20 p-4">
              <div className="flex flex-col gap-3 md:flex-row md:items-start md:justify-between">
                <div>
                  <div className="text-sm font-medium text-founder-ink">{project.name}</div>
                  <p className="mt-2 text-sm leading-6 text-muted">{project.description}</p>
                </div>
                <span className="rounded-md border border-border px-2.5 py-1 text-xs text-muted">{project.stage}</span>
              </div>
              <div className="mt-4 flex items-center gap-2 text-xs text-muted">
                <CalendarDays className="h-3.5 w-3.5" />
                Updated {new Date(project.updated_at).toLocaleDateString()}
              </div>
            </div>
          ))}
        </div>
      </GlassCard>
    </div>
  );
}
