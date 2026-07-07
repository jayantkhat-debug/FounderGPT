import Link from "next/link";

import { AppShell } from "@/components/layout/app-shell";
import { Button } from "@/components/ui/button";

type PlaceholderPageProps = {
  title: string;
  description: string;
  ctaHref?: string;
  ctaLabel?: string;
};

export function PlaceholderPage({
  title,
  description,
  ctaHref = "/projects",
  ctaLabel = "Open projects",
}: PlaceholderPageProps) {
  return (
    <AppShell
      header={
        <header className="border-b border-border pb-5">
          <h1 className="text-3xl font-semibold text-founder-ink md:text-4xl">{title}</h1>
          <p className="mt-3 max-w-2xl text-sm leading-6 text-muted md:text-base">{description}</p>
        </header>
      }
    >
      <div className="rounded-lg border border-border bg-white/[0.04] p-6">
        <p className="text-sm leading-6 text-muted">This workspace is coming soon. Use Projects and AI Chat today.</p>
        <Button asChild className="mt-4">
          <Link href={ctaHref}>{ctaLabel}</Link>
        </Button>
      </div>
    </AppShell>
  );
}
