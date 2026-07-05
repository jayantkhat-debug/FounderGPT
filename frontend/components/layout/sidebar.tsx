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

const navItems = [
  { label: "Dashboard", icon: LayoutDashboard },
  { label: "Projects", icon: FolderKanban },
  { label: "AI Chat", icon: Bot },
  { label: "Business Plan", icon: FileText },
  { label: "Pitch Deck", icon: BarChart3 },
  { label: "Market Research", icon: LineChart },
  { label: "Competitors", icon: Users },
  { label: "Financial Model", icon: BriefcaseBusiness },
  { label: "YC Application", icon: ClipboardList },
  { label: "Investor CRM", icon: Landmark },
  { label: "Tasks", icon: CalendarDays },
  { label: "Settings", icon: Settings },
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
            <button
              key={item.label}
              className={`flex h-10 w-full items-center gap-3 rounded-md px-3 text-left text-sm transition ${
                active ? "bg-white/10 text-founder-ink" : "text-muted hover:bg-white/[0.07] hover:text-founder-ink"
              }`}
            >
              <Icon className="h-4 w-4" aria-hidden />
              {item.label}
            </button>
          );
        })}
      </nav>
    </aside>
  );
}
