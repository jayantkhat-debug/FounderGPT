import { AppShell } from "@/components/layout/app-shell";
import { ProjectWorkspace } from "@/components/founder/project-workspace";

export default function ProjectsPage() {
  return (
    <AppShell
      header={
        <header className="border-b border-border pb-5">
          <div className="text-sm font-semibold text-founder-cyan">FounderGPT X Projects</div>
          <h1 className="mt-3 text-3xl font-semibold text-founder-ink md:text-5xl">Build every startup in its own workspace.</h1>
          <p className="mt-3 max-w-2xl text-sm leading-6 text-muted md:text-base">
            Create startup projects, preserve founder memory, and restore each project conversation from PostgreSQL.
          </p>
        </header>
      }
    >
      <ProjectWorkspace />
    </AppShell>
  );
}
