"use client";

import { ClerkProvider } from "@clerk/nextjs";
import { ApiHealth } from "@/components/ui/api-health";

export function Providers({ children }: Readonly<{ children: React.ReactNode }>) {
  // show API health banner regardless of Clerk usage
  const content = (
    <>
      <ApiHealth />
      {children}
    </>
  );

  if (!process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY) {
    return <>{content}</>;
  }

  return <ClerkProvider>{content}</ClerkProvider>;
}
