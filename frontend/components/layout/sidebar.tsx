"use client";

import {
  BarChart3,
  Bot,
  BriefcaseBusiness,
  CalendarDays,
  ClipboardList,
  FileText,
  FolderKanban,
  Landmark,
  LayoutDashboard,
  LineChart,
  Menu,
  Settings,
  Users,
  X,
} from "lucide-react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";

import { AuthActions } from "@/components/layout/auth-actions";

const navItems = [
  { label: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
  { label: "Projects", href: "/projects", icon: FolderKanban },
  { label: "AI Chat", href: "/ai-chat", icon: Bot },
  { label: "Business Plan", href: "/business-plan", icon: FileText },
  { label: "Pitch Deck", href: "/pitch-deck", icon: BarChart3 },
  { label: "Market Research", href: "/market-research", icon: LineChart },
  { label: "Competitors", href: "/competitors", icon: Users },
  { label: "Financial Model", href: "/financial-model", icon: BriefcaseBusiness },
  { label: "YC Application", href: "/yc-application", icon: ClipboardList },
  { label: "Investor CRM", href: "/investor-crm", icon: Landmark },
  { label: "Tasks", href: "/tasks", icon: CalendarDays },
  { label: "Settings", href: "/settings", icon: Settings },
];

function isNavActive(pathname: string, href: string) {
  if (href === "/dashboard") {
    return pathname === "/" || pathname === "/dashboard";
  }

  return pathname === href || pathname.startsWith(`${href}/`);
}

function SidebarNav({ onNavigate }: { onNavigate?: () => void }) {
  const pathname = usePathname();

  return (
    <nav className="space-y-1">
      {navItems.map((item) => {
        const Icon = item.icon;
        const active = isNavActive(pathname, item.href);

        return (
          <Link
            href={item.href}
            key={item.label}
            onClick={onNavigate}
            className={`flex h-10 w-full items-center gap-3 rounded-md px-3 text-left text-sm transition ${
              active ? "bg-white/10 text-founder-ink" : "text-muted hover:bg-white/[0.07] hover:text-founder-ink"
            }`}
          >
            <Icon className="h-4 w-4" aria-hidden />
            {item.label}
          </Link>
        );
      })}
    </nav>
  );
}

export function Sidebar() {
  const [mobileOpen, setMobileOpen] = useState(false);

  return (
    <>
      <div className="fixed inset-x-0 top-0 z-40 flex h-14 items-center justify-between border-b border-border bg-background/95 px-4 backdrop-blur-xl lg:hidden">
        <div>
          <div className="text-sm font-semibold text-founder-ink">FounderGPT X</div>
          <div className="text-xs text-muted">The AI Operating System for Founders</div>
        </div>
        <button
          type="button"
          aria-label={mobileOpen ? "Close navigation menu" : "Open navigation menu"}
          onClick={() => setMobileOpen((open) => !open)}
          className="inline-flex h-10 w-10 items-center justify-center rounded-md border border-border text-founder-ink transition hover:bg-white/[0.08]"
        >
          {mobileOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
        </button>
      </div>

      {mobileOpen ? (
        <button
          type="button"
          aria-label="Close navigation menu"
          className="fixed inset-0 z-40 bg-black/60 lg:hidden"
          onClick={() => setMobileOpen(false)}
        />
      ) : null}

      <aside
        className={`fixed inset-y-0 left-0 z-50 w-72 border-r border-border bg-background px-4 py-5 backdrop-blur-xl transition-transform lg:static lg:block lg:min-h-screen lg:translate-x-0 ${
          mobileOpen ? "translate-x-0" : "-translate-x-full"
        }`}
      >
        <div className="mb-8 hidden px-2 lg:block">
          <div className="text-sm font-semibold text-founder-ink">FounderGPT X</div>
          <div className="mt-1 text-xs text-muted">The AI Operating System for Founders</div>
        </div>
        <SidebarNav onNavigate={() => setMobileOpen(false)} />
        <div className="mt-8 border-t border-border pt-4">
          <AuthActions />
        </div>
      </aside>
    </>
  );
}
