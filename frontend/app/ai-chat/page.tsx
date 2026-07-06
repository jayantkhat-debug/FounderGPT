import { StartupChat } from "@/components/founder/startup-chat";

export default function AiChatPage() {
  return (
    <div className="p-8">
      <h1 className="text-2xl font-semibold">AI Chat</h1>
      <p className="mt-3 text-sm text-muted">Use the AI agent to pressure test ideas and get founder guidance.</p>
      <div className="mt-6">
        <StartupChat />
      </div>
    </div>
  );
}
