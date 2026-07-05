import { Sidebar } from "@/components/layout/sidebar";
import { ProjectWorkspace } from "@/components/founder/project-workspace";

export default function ProjectsPage() {
  return (
    <div className="flex min-h-screen bg-background">
      <Sidebar />
      <main className="relative flex-1 overflow-hidden">
        <div className="absolute inset-x-0 top-0 h-80 bg-[radial-gradient(circle_at_top,rgba(125,231,255,0.16),transparent_55%)]" />
        <div className="relative mx-auto flex w-full max-w-7xl flex-col gap-6 px-5 py-5 sm:px-8 lg:px-10">
          <header className="border-b border-border pb-5">
            <div className="text-sm font-semibold text-founder-cyan">FounderGPT X Projects</div>
            <h1 className="mt-3 text-3xl font-semibold text-founder-ink md:text-5xl">Build every startup in its own workspace.</h1>
            <p className="mt-3 max-w-2xl text-sm leading-6 text-muted md:text-base">
              Create startup projects, preserve founder memory, and restore each project conversation from PostgreSQL.
            </p>
          </header>
          <ProjectWorkspace />
        </div>
      </main>
    </div>
  );
}
