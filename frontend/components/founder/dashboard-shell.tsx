"use client";

import { motion } from "framer-motion";
import { ArrowUpRight, CheckCircle2, CircleAlert, Sparkles } from "lucide-react";

import { AppShell } from "@/components/layout/app-shell";
import { StartupChat } from "@/components/founder/startup-chat";
import { Button } from "@/components/ui/button";
import { GlassCard } from "@/components/ui/glass-card";

const metrics = [
  { label: "Validation Score", value: "72", detail: "Customer proof needed" },
  { label: "Runway", value: "8 mo", detail: "Default scenario" },
  { label: "Investor Readiness", value: "41%", detail: "Narrative too broad" },
  { label: "Weekly Focus", value: "3", detail: "Critical moves" },
];

export function DashboardShell() {
  function scrollToChat() {
    document.getElementById("founder-chat")?.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  return (
    <AppShell
      header={
        <header className="flex flex-col gap-4 border-b border-border pb-5 md:flex-row md:items-center md:justify-between">
          <div>
            <div className="mb-2 inline-flex items-center gap-2 rounded-md border border-border bg-white/[0.05] px-2.5 py-1 text-xs text-muted">
              <Sparkles className="h-3.5 w-3.5 text-founder-cyan" />
              FounderGPT X
            </div>
            <h1 className="text-3xl font-semibold tracking-normal text-founder-ink md:text-5xl">
              From idea to funded startup.
            </h1>
            <p className="mt-3 max-w-2xl text-sm leading-6 text-muted md:text-base">
              The AI Operating System for Founders. Build. Validate. Launch. Fund.
            </p>
          </div>
          <Button type="button" onClick={scrollToChat} className="w-full gap-2 md:w-auto">
            Start founder interview
            <ArrowUpRight className="h-4 w-4" />
          </Button>
        </header>
      }
      footer={
        <footer className="border-t border-border py-5 text-xs text-muted">
          FounderGPT X. Copyright © 2026. All Rights Reserved.
        </footer>
      }
    >
      <section className="grid gap-3 md:grid-cols-4">
        {metrics.map((metric) => (
          <GlassCard key={metric.label} className="min-h-32">
            <div className="text-xs uppercase tracking-[0.16em] text-muted">{metric.label}</div>
            <div className="mt-4 text-3xl font-semibold text-founder-ink">{metric.value}</div>
            <div className="mt-2 text-sm text-muted">{metric.detail}</div>
          </GlassCard>
        ))}
      </section>

      <section className="grid gap-5 xl:grid-cols-[1.15fr_0.85fr]">
        <motion.div id="founder-chat" initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }}>
          <StartupChat />
        </motion.div>

        <div className="grid gap-5">
          <GlassCard>
            <div className="text-sm font-medium text-founder-ink">FounderGPT X</div>
            <div className="mt-3 text-sm leading-6 text-muted">
              AI-powered. Founder-first. Built for disciplined startup execution.
            </div>
          </GlassCard>

          <GlassCard>
            <div className="flex items-center gap-2 text-sm font-medium text-founder-ink">
              <CircleAlert className="h-4 w-4 text-founder-violet" />
              Critical risks
            </div>
            <div className="mt-4 space-y-3 text-sm text-muted">
              <p>Target customer is still too broad.</p>
              <p>No paid validation captured in memory.</p>
              <p>Investor narrative needs a sharper wedge.</p>
            </div>
          </GlassCard>

          <GlassCard>
            <div className="flex items-center gap-2 text-sm font-medium text-founder-ink">
              <CheckCircle2 className="h-4 w-4 text-founder-green" />
              This week
            </div>
            <div className="mt-4 space-y-3 text-sm text-muted">
              <p>Interview 5 narrowly defined buyers.</p>
              <p>Ship one onboarding path.</p>
              <p>Draft a VC-style problem narrative.</p>
            </div>
          </GlassCard>
        </div>
      </section>
    </AppShell>
  );
}
