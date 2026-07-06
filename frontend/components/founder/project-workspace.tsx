"use client";

import { FormEvent, useCallback, useEffect, useState } from "react";
import { useAuth } from "@clerk/nextjs";
import { CalendarDays, FolderKanban, Loader2, Plus, Briefcase, Sparkles, Landmark, FileText, Globe } from "lucide-react";

import { Button } from "@/components/ui/button";
import { GlassCard } from "@/components/ui/glass-card";
import { createProject, listProjects, generateBusinessModel, generateFinancialModel, generateBusinessPlan, generateWeb3Strategy, type Project } from "@/lib/api";

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
  const [isGenerating, setIsGenerating] = useState<string | null>(null);
  const [isGeneratingFinance, setIsGeneratingFinance] = useState<string | null>(null);
  const [isGeneratingPlan, setIsGeneratingPlan] = useState<string | null>(null);
  const [isGeneratingWeb3, setIsGeneratingWeb3] = useState<string | null>(null);
  const [businessModels, setBusinessModels] = useState<Record<string, string>>({});
  const [financialModels, setFinancialModels] = useState<Record<string, string>>({});
  const [businessPlans, setBusinessPlans] = useState<Record<string, string>>({});
  const [web3Strategies, setWeb3Strategies] = useState<Record<string, string>>({});
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

  async function handleGenerateBusinessModel(projectId: string) {
    if (isGenerating) return;

    setIsGenerating(projectId);
    setError(null);
    try {
      const token = await resolveToken();
      const result = await generateBusinessModel(projectId, token);
      setBusinessModels((current) => ({
        ...current,
        [projectId]: result.business_model,
      }));
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Could not generate business model.");
    } finally {
      setIsGenerating(null);
    }
  }

  async function handleGenerateFinancialModel(projectId: string) {
    if (isGeneratingFinance) return;

    setIsGeneratingFinance(projectId);
    setError(null);
    try {
      const token = await resolveToken();
      const result = await generateFinancialModel(projectId, token);
      setFinancialModels((current) => ({
        ...current,
        [projectId]: result.financial_model,
      }));
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Could not generate financial model.");
    } finally {
      setIsGeneratingFinance(null);
    }
  }

  async function handleGenerateBusinessPlan(projectId: string) {
    if (isGeneratingPlan) return;

    setIsGeneratingPlan(projectId);
    setError(null);
    try {
      const token = await resolveToken();
      const result = await generateBusinessPlan(projectId, token);
      setBusinessPlans((current) => ({
        ...current,
        [projectId]: result.business_plan,
      }));
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Could not generate business plan.");
    } finally {
      setIsGeneratingPlan(null);
    }
  }

  async function handleGenerateWeb3Strategy(projectId: string) {
    if (isGeneratingWeb3) return;

    setIsGeneratingWeb3(projectId);
    setError(null);
    try {
      const token = await resolveToken();
      const result = await generateWeb3Strategy(projectId, token);
      setWeb3Strategies((current) => ({
        ...current,
        [projectId]: result.web3_strategy,
      }));
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Could not generate Web3 strategy.");
    } finally {
      setIsGeneratingWeb3(null);
    }
  }

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

              <div className="mt-4 grid gap-3 md:grid-cols-2">
                {businessModels[project.id] && (
                  <div className="rounded-md border border-founder-cyan/20 bg-founder-cyan/5 p-4 text-sm text-founder-ink">
                    <div className="mb-2 flex items-center gap-2 font-medium text-founder-cyan">
                      <Briefcase className="h-4 w-4" />
                      Business Model
                    </div>
                    <div className="max-h-60 overflow-y-auto whitespace-pre-wrap text-muted text-xs leading-5">
                      {businessModels[project.id]}
                    </div>
                  </div>
                )}

                {financialModels[project.id] && (
                  <div className="rounded-md border border-founder-violet/20 bg-founder-violet/5 p-4 text-sm text-founder-ink">
                    <div className="mb-2 flex items-center gap-2 font-medium text-founder-violet">
                      <Landmark className="h-4 w-4" />
                      Financial Model
                    </div>
                    <div className="max-h-60 overflow-y-auto whitespace-pre-wrap text-muted text-xs leading-5">
                      {financialModels[project.id]}
                    </div>
                  </div>
                )}

                {businessPlans[project.id] && (
                  <div className="rounded-md border border-founder-green/20 bg-founder-green/5 p-4 text-sm text-founder-ink md:col-span-2">
                    <div className="mb-2 flex items-center gap-2 font-medium text-founder-green">
                      <FileText className="h-4 w-4" />
                      Business Plan
                    </div>
                    <div className="max-h-80 overflow-y-auto whitespace-pre-wrap text-muted text-xs leading-5">
                      {businessPlans[project.id]}
                    </div>
                  </div>
                )}

                {web3Strategies[project.id] && (
                  <div className="rounded-md border border-founder-cyan/20 bg-founder-cyan/5 p-4 text-sm text-founder-ink md:col-span-2">
                    <div className="mb-2 flex items-center gap-2 font-medium text-founder-cyan">
                      <Globe className="h-4 w-4" />
                      Web3 Strategy
                    </div>
                    <div className="max-h-60 overflow-y-auto whitespace-pre-wrap text-muted text-xs leading-5">
                      {web3Strategies[project.id]}
                    </div>
                  </div>
                )}
              </div>

              <div className="mt-4 flex flex-col gap-3 lg:flex-row lg:items-center lg:justify-between">
                <div className="flex items-center gap-2 text-xs text-muted">
                  <CalendarDays className="h-3.5 w-3.5" />
                  Updated {new Date(project.updated_at).toLocaleDateString()}
                </div>
                <div className="flex flex-wrap gap-2">
                  <Button
                    variant="secondary"
                    className="h-8 gap-2 text-xs"
                    onClick={() => handleGenerateBusinessModel(project.id)}
                    disabled={isGenerating === project.id}
                  >
                    {isGenerating === project.id ? (
                      <Loader2 className="h-3 w-3 animate-spin" />
                    ) : (
                      <Briefcase className="h-3 w-3 text-founder-cyan" />
                    )}
                    {businessModels[project.id] ? "Update Business" : "Gen Business"}
                  </Button>
                  <Button
                    variant="secondary"
                    className="h-8 gap-2 text-xs"
                    onClick={() => handleGenerateFinancialModel(project.id)}
                    disabled={isGeneratingFinance === project.id}
                  >
                    {isGeneratingFinance === project.id ? (
                      <Loader2 className="h-3 w-3 animate-spin" />
                    ) : (
                      <Landmark className="h-3 w-3 text-founder-violet" />
                    )}
                    {financialModels[project.id] ? "Update Finance" : "Gen Finance"}
                  </Button>
                  <Button
                    variant="secondary"
                    className="h-8 gap-2 text-xs"
                    onClick={() => handleGenerateBusinessPlan(project.id)}
                    disabled={isGeneratingPlan === project.id}
                  >
                    {isGeneratingPlan === project.id ? (
                      <Loader2 className="h-3 w-3 animate-spin" />
                    ) : (
                      <FileText className="h-3 w-3 text-founder-green" />
                    )}
                    {businessPlans[project.id] ? "Update Plan" : "Gen Plan"}
                  </Button>
                  <Button
                    variant="secondary"
                    className="h-8 gap-2 text-xs"
                    onClick={() => handleGenerateWeb3Strategy(project.id)}
                    disabled={isGeneratingWeb3 === project.id}
                  >
                    {isGeneratingWeb3 === project.id ? (
                      <Loader2 className="h-3 w-3 animate-spin" />
                    ) : (
                      <Globe className="h-3 w-3 text-founder-cyan" />
                    )}
                    {web3Strategies[project.id] ? "Update Web3" : "Gen Web3"}
                  </Button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </GlassCard>
    </div>
  );
}
