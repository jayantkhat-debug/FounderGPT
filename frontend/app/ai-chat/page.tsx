import { AppShell } from "@/components/layout/app-shell";
import { StartupChat } from "@/components/founder/startup-chat";

export default function AiChatPage() {
  return (
    <AppShell
      header={
        <header className="border-b border-border pb-5">
          <h1 className="text-3xl font-semibold text-founder-ink md:text-4xl">AI Chat</h1>
          <p className="mt-3 max-w-2xl text-sm leading-6 text-muted md:text-base">
            Use the AI agent to pressure test ideas and get founder guidance.
          </p>
        </header>
      }
    >
      <StartupChat />
    </AppShell>
  );
}
