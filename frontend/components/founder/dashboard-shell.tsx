"use client";

import { motion } from "framer-motion";
import { ArrowUpRight, BrainCircuit, CheckCircle2, CircleAlert, Sparkles } from "lucide-react";

import { Sidebar } from "@/components/layout/sidebar";
import { Button } from "@/components/ui/button";
import { GlassCard } from "@/components/ui/glass-card";

const metrics = [
  { label: "Validation Score", value: "72", detail: "Customer proof needed" },
  { label: "Runway", value: "8 mo", detail: "Default scenario" },
  { label: "Investor Readiness", value: "41%", detail: "Narrative too broad" },
  { label: "Weekly Focus", value: "3", detail: "Critical moves" },
];

const agents = ["CEO", "CTO", "Product", "VC", "Marketing", "Finance", "Legal", "UX"];

export function DashboardShell() {
  return (
    <div className="flex min-h-screen bg-background">
      <Sidebar />
      <main className="relative flex-1 overflow-hidden">
        <div className="absolute inset-x-0 top-0 h-80 bg-[radial-gradient(circle_at_top,rgba(125,231,255,0.16),transparent_55%)]" />
        <div className="relative mx-auto flex w-full max-w-7xl flex-col gap-6 px-5 py-5 sm:px-8 lg:px-10">
          <header className="flex flex-col gap-4 border-b border-border pb-5 md:flex-row md:items-center md:justify-between">
            <div>
              <div className="mb-2 inline-flex items-center gap-2 rounded-md border border-border bg-white/[0.05] px-2.5 py-1 text-xs text-muted">
                <Sparkles className="h-3.5 w-3.5 text-founder-cyan" />
                Phase 1 command center
              </div>
              <h1 className="text-3xl font-semibold tracking-normal text-founder-ink md:text-5xl">
                Build the startup that can survive investor scrutiny.
              </h1>
              <p className="mt-3 max-w-2xl text-sm leading-6 text-muted md:text-base">
                FounderGPT X interviews, challenges, and turns founder context into strategy, tasks, documents, and fundraising assets.
              </p>
            </div>
            <Button className="w-full gap-2 md:w-auto">
              Start founder interview
              <ArrowUpRight className="h-4 w-4" />
            </Button>
          </header>

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
            <GlassCard className="p-0">
              <div className="border-b border-border p-5">
                <div className="flex items-center gap-2 text-sm font-medium text-founder-ink">
                  <BrainCircuit className="h-4 w-4 text-founder-cyan" />
                  AI boardroom
                </div>
                <p className="mt-2 text-sm text-muted">
                  Each agent gets its own operating style and pushes against weak assumptions.
                </p>
              </div>
              <div className="grid gap-2 p-5 sm:grid-cols-2">
                {agents.map((agent, index) => (
                  <motion.div
                    key={agent}
                    initial={{ opacity: 0, y: 8 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: index * 0.03 }}
                    className="rounded-md border border-border bg-black/20 p-4"
                  >
                    <div className="text-sm font-medium text-founder-ink">{agent}</div>
                    <div className="mt-1 text-xs leading-5 text-muted">
                      {agent === "VC" ? "Finds investor objections before investors do." : "Turns founder context into concrete next moves."}
                    </div>
                  </motion.div>
                ))}
              </div>
            </GlassCard>

            <div className="grid gap-5">
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
        </div>
      </main>
    </div>
  );
}
