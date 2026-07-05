"use client";

import { SignInButton, SignOutButton, SignedIn, SignedOut, UserButton } from "@clerk/nextjs";

import { Button } from "@/components/ui/button";

export function AuthActions() {
  if (!process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY) {
    return <div className="rounded-md border border-border px-3 py-2 text-xs text-muted">Dev auth</div>;
  }

  return (
    <div className="flex items-center gap-2">
      <SignedIn>
        <UserButton afterSignOutUrl="/" />
        <SignOutButton>
          <Button variant="ghost" className="h-8 px-3 text-xs">
            Logout
          </Button>
        </SignOutButton>
      </SignedIn>
      <SignedOut>
        <SignInButton mode="modal">
          <Button variant="secondary" className="h-8 px-3 text-xs">
            Login
          </Button>
        </SignInButton>
      </SignedOut>
    </div>
  );
}
