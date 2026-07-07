import { Sidebar } from "@/components/layout/sidebar";

type AppShellProps = {
  children: React.ReactNode;
  header?: React.ReactNode;
  footer?: React.ReactNode;
};

export function AppShell({ children, header, footer }: AppShellProps) {
  return (
    <div className="flex min-h-screen bg-background">
      <Sidebar />
      <main className="relative flex-1 overflow-hidden pt-14 lg:pt-0">
        <div className="absolute inset-x-0 top-0 h-80 bg-[radial-gradient(circle_at_top,rgba(125,231,255,0.16),transparent_55%)]" />
        <div className="relative mx-auto flex w-full max-w-7xl flex-col gap-6 px-5 py-5 sm:px-8 lg:px-10">
          {header}
          {children}
          {footer}
        </div>
      </main>
    </div>
  );
}
