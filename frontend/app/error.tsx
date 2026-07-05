"use client";

import { Button } from "@/components/ui/button";

export default function ErrorPage({ reset }: { reset: () => void }) {
  return (
    <main className="flex min-h-screen items-center justify-center bg-background px-6 text-center">
      <div className="max-w-md">
        <div className="text-sm font-semibold text-founder-cyan">500</div>
        <h1 className="mt-3 text-3xl font-semibold text-founder-ink">FounderGPT X hit an unexpected issue.</h1>
        <p className="mt-3 text-sm leading-6 text-muted">
          The AI Operating System for Founders is still running. Retry the page when you are ready.
        </p>
        <Button onClick={reset} className="mt-6">
          Retry FounderGPT X
        </Button>
      </div>
    </main>
  );
}
