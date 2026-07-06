"use client";

import { useEffect, useState } from "react";

export function ApiHealth() {
  const [status, setStatus] = useState<"unknown" | "ok" | "down">("unknown");
  const apiBase = process.env.NEXT_PUBLIC_API_BASE_URL;

  async function check() {
    if (!apiBase) {
      setStatus("down");
      return;
    }

    try {
      const controller = new AbortController();
      const id = setTimeout(() => controller.abort(), 4000);
      const res = await fetch(`${apiBase}/health`, { signal: controller.signal });
      clearTimeout(id);
      if (!res.ok) throw new Error("non-ok");
      setStatus("ok");
      // expose for other code to check
      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-ignore
      window.__FGPT_API_OK = true;
    } catch (err) {
      setStatus("down");
      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-ignore
      window.__FGPT_API_OK = false;
    }
  }

  useEffect(() => {
    check();
    const id = setInterval(check, 30_000);
    return () => clearInterval(id);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  if (status === "ok") return null;

  return (
    <div className="fixed left-0 right-0 top-0 z-50 bg-yellow-500/95 text-black p-3 text-sm text-center">
      <div className="max-w-4xl mx-auto flex items-center justify-center gap-3">
        <div>API appears unreachable. Some features (AI agent, saves) may not work.</div>
        <button
          className="rounded bg-black/10 px-3 py-1 text-xs"
          onClick={() => {
            // re-run check
            void check();
          }}
        >
          Retry
        </button>
      </div>
    </div>
  );
}
