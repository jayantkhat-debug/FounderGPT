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
  Settings,
  Users,
} from "lucide-react";
import Link from "next/link";

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

export function Sidebar() {
  return (
    <aside className="hidden min-h-screen w-72 border-r border-border bg-white/[0.035] px-4 py-5 backdrop-blur-xl lg:block">
      <div className="mb-8 px-2">
        <div className="text-sm font-semibold text-founder-ink">FounderGPT X</div>
        <div className="mt-1 text-xs text-muted">The AI Operating System for Founders</div>
      </div>
      <nav className="space-y-1">
        {navItems.map((item, index) => {
          const Icon = item.icon;
          const active = index === 0;
          return (
            <Link
              href={item.href}
              key={item.label}
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
      <div className="mt-8 border-t border-border pt-4">
        <AuthActions />
      </div>
    </aside>
  );
}
