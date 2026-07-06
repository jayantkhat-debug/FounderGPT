import type { Metadata } from "next";

import "./globals.css";
import { Providers } from "./providers";

export const metadata: Metadata = {
  title: "FounderGPT X",
  description: "FounderGPT X — The AI Operating System for Founders.",
  applicationName: "FounderGPT X",
  authors: [{ name: "FounderGPT X" }],
  creator: "FounderGPT X",
  publisher: "FounderGPT X",
  openGraph: {
    title: "FounderGPT X",
    description: "FounderGPT X — The AI Operating System for Founders.",
    siteName: "FounderGPT X",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "FounderGPT X",
    description: "The AI Operating System for Founders.",
  },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className="dark">
      {/* suppressHydrationWarning prevents React from erroring when browser extensions inject attributes into the DOM before hydration (e.g., Grammarly) */}
      <body suppressHydrationWarning>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
