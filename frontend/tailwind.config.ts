import type { Config } from "tailwindcss";
import animatePlugin from "tailwindcss-animate";

const config: Config = {
  darkMode: ["class"],
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}", "./lib/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        background: "#050608",
        surface: "#0d1017",
        border: "rgba(255,255,255,0.10)",
        muted: "#8f98aa",
        founder: {
          cyan: "#7de7ff",
          green: "#8bffbd",
          ink: "#f5f7fb",
          violet: "#a78bfa"
        }
      },
      boxShadow: {
        glow: "0 0 60px rgba(125, 231, 255, 0.16)"
      },
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui", "sans-serif"]
      }
    }
  },
  plugins: [animatePlugin]
};

export default config;
