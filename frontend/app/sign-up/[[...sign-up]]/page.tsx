import { SignUp } from "@clerk/nextjs";

export default function SignUpPage() {
  if (!process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY) {
    return (
      <main className="flex min-h-screen items-center justify-center bg-background px-6 text-center">
        <div className="max-w-md">
          <h1 className="text-3xl font-semibold text-founder-ink">Create a FounderGPT X account</h1>
          <p className="mt-3 text-sm leading-6 text-muted">
            Clerk is not configured locally. Add `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` to enable sign up.
          </p>
        </div>
      </main>
    );
  }

  return (
    <main className="flex min-h-screen items-center justify-center bg-background px-6">
      <SignUp routing="path" path="/sign-up" signInUrl="/sign-in" />
    </main>
  );
}
