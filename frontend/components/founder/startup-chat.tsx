"use client";

import { FormEvent, useEffect, useRef, useState } from "react";
import { AlertCircle, Loader2, Send, Sparkles } from "lucide-react";

import { Button } from "@/components/ui/button";
import { GlassCard } from "@/components/ui/glass-card";
import { type ConversationMessage, evaluateStartupIdea } from "@/lib/api";
import { cn } from "@/lib/utils";

const starterMessages: ConversationMessage[] = [
  {
    role: "assistant",
    content:
      "Tell me the startup idea. I will pressure-test the customer, market, wedge, business model, and next moves.",
  },
];

export function StartupChat() {
  const [startupIdea, setStartupIdea] = useState("");
  const [messages, setMessages] = useState<ConversationMessage[]>(starterMessages);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const endRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth", block: "end" });
  }, [messages, isLoading]);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const trimmedIdea = startupIdea.trim();
    if (trimmedIdea.length < 10 || isLoading) {
      return;
    }

    const userMessage: ConversationMessage = {
      role: "user",
      content: trimmedIdea,
    };

    setMessages((current) => [...current, userMessage]);
    setStartupIdea("");
    setError(null);
    setIsLoading(true);

    try {
      const result = await evaluateStartupIdea({
        startupIdea: trimmedIdea,
        conversationHistory: messages.slice(1),
      });

      setMessages((current) => [
        ...current,
        {
          role: "assistant",
          content: result.response,
        },
      ]);
    } catch (caught) {
      const message = caught instanceof Error ? caught.message : "FounderGPT X could not respond. Please retry.";
      setError(message);
      setMessages((current) => current.filter((item) => item !== userMessage));
      setStartupIdea(trimmedIdea);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <GlassCard className="flex min-h-[620px] flex-col p-0">
      <div className="border-b border-border p-5">
        <div className="flex items-center gap-2 text-sm font-medium text-founder-ink">
          <Sparkles className="h-4 w-4 text-founder-cyan" />
          FounderGPT X chat
        </div>
        <p className="mt-2 text-sm leading-6 text-muted">
          Send a startup idea and get a direct AI co-founder response powered by NVIDIA Build API.
        </p>
      </div>

      <div className="flex-1 space-y-4 overflow-y-auto p-5">
        {messages.map((message, index) => {
          const isUser = message.role === "user";
          return (
            <div key={`${message.role}-${index}`} className={cn("flex", isUser ? "justify-end" : "justify-start")}>
              <div
                className={cn(
                  "max-w-[88%] rounded-lg border px-4 py-3 text-sm leading-6 shadow-sm md:max-w-[78%]",
                  isUser
                    ? "border-founder-cyan/30 bg-founder-cyan/10 text-founder-ink"
                    : "border-border bg-black/25 text-founder-ink",
                )}
              >
                <div className="mb-1 text-xs font-medium text-muted">{isUser ? "Founder" : "FounderGPT X"}</div>
                <div className="whitespace-pre-wrap">{message.content}</div>
              </div>
            </div>
          );
        })}

        {isLoading ? (
          <div className="flex justify-start">
            <div className="flex max-w-[78%] items-center gap-3 rounded-lg border border-border bg-black/25 px-4 py-3 text-sm text-muted">
              <Loader2 className="h-4 w-4 animate-spin text-founder-cyan" />
              Thinking like a skeptical co-founder...
            </div>
          </div>
        ) : null}
        <div ref={endRef} />
      </div>

      {error ? (
        <div className="mx-5 mb-4 flex items-start gap-2 rounded-md border border-red-400/25 bg-red-500/10 p-3 text-sm leading-6 text-red-100">
          <AlertCircle className="mt-0.5 h-4 w-4 shrink-0" />
          <span>{error}</span>
        </div>
      ) : null}

      <form onSubmit={handleSubmit} className="border-t border-border p-5">
        <div className="flex flex-col gap-3">
          <textarea
            value={startupIdea}
            onChange={(event) => setStartupIdea(event.target.value)}
            placeholder="Example: I am building an AI operating system that helps first-time founders validate ideas, create investor materials, and manage execution."
            className="min-h-28 resize-none rounded-lg border border-border bg-black/30 px-4 py-3 text-sm leading-6 text-founder-ink outline-none transition placeholder:text-muted focus:border-founder-cyan/45 focus:ring-2 focus:ring-founder-cyan/15"
          />
          <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
            <p className="text-xs leading-5 text-muted">
              FounderGPT X will challenge assumptions before giving advice.
            </p>
            <Button type="submit" disabled={startupIdea.trim().length < 10 || isLoading} className="gap-2">
              {isLoading ? <Loader2 className="h-4 w-4 animate-spin" /> : <Send className="h-4 w-4" />}
              Send idea
            </Button>
          </div>
        </div>
      </form>
    </GlassCard>
  );
}
