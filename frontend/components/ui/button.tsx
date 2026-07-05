import { Slot } from "@radix-ui/react-slot";
import { type ButtonHTMLAttributes } from "react";

import { cn } from "@/lib/utils";

type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  asChild?: boolean;
  variant?: "primary" | "secondary" | "ghost";
};

export function Button({ asChild, className, variant = "primary", ...props }: ButtonProps) {
  const Comp = asChild ? Slot : "button";

  return (
    <Comp
      className={cn(
        "inline-flex h-10 items-center justify-center rounded-md px-4 text-sm font-medium transition focus:outline-none focus:ring-2 focus:ring-founder-cyan/50 disabled:pointer-events-none disabled:opacity-50",
        variant === "primary" && "bg-founder-ink text-background hover:bg-white",
        variant === "secondary" && "border border-border bg-white/[0.08] text-founder-ink hover:bg-white/[0.12]",
        variant === "ghost" && "text-muted hover:bg-white/[0.08] hover:text-founder-ink",
        className,
      )}
      {...props}
    />
  );
}
