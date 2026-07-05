import { Button } from "@/components/ui/button";

export default function NotFound() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-background px-6 text-center">
      <div className="max-w-md">
        <div className="text-sm font-semibold text-founder-cyan">404</div>
        <h1 className="mt-3 text-3xl font-semibold text-founder-ink">FounderGPT X could not find this page.</h1>
        <p className="mt-3 text-sm leading-6 text-muted">
          Return to the AI Operating System for Founders and keep building.
        </p>
        <Button asChild className="mt-6">
          <a href="/">Back to FounderGPT X</a>
        </Button>
      </div>
    </main>
  );
}
