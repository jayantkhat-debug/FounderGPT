import { type HTMLAttributes } from "react";

import { cn } from "@/lib/utils";

export function GlassCard({ className, ...props }: HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={cn(
        "rounded-lg border border-border bg-white/[0.055] p-5 shadow-glow backdrop-blur-xl",
        className,
      )}
      {...props}
    />
  );
}
