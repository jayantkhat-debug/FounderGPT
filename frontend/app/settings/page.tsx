import Link from "next/link";

import { AppShell } from "@/components/layout/app-shell";
import { Button } from "@/components/ui/button";

export default function SettingsPage() {
  return (
    <AppShell
      header={
        <header className="border-b border-border pb-5">
          <h1 className="text-3xl font-semibold text-founder-ink md:text-4xl">Settings</h1>
          <p className="mt-3 max-w-2xl text-sm leading-6 text-muted md:text-base">
            Account and workspace settings will live here.
          </p>
        </header>
      }
    >
      <div className="rounded-lg border border-border bg-white/[0.04] p-6">
        <p className="text-sm leading-6 text-muted">
          Authentication is handled through Clerk when configured. Project data is stored in the FounderGPT X backend.
        </p>
        <Button asChild className="mt-4">
          <Link href="/projects">Manage projects</Link>
        </Button>
      </div>
    </AppShell>
  );
}
