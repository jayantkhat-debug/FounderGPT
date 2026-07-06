# FounderGPT X Frontend

Next.js 15 App Router frontend for FounderGPT X. Designed for deployment on Vercel.

## Local Development

### Setup

```bash
npm install
```

### Configuration

Create `.env.local` (copy from `.env.example`):

```bash
cp .env.example .env.local
```

For local development with backend running on `http://127.0.0.1:8000`:

```
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000/api/v1
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=  # Leave empty for dev mode
NEXT_PUBLIC_DEV_API_TOKEN=dev
```

### Run Locally

```bash
npm run dev
```

Open `http://localhost:3000`

### Type Check

```bash
npm run typecheck
```

### Build for Production

```bash
npm run build
```

## Production Deployment on Vercel

### Prerequisites

- Vercel account
- GitHub repository connected to Vercel
- Railway backend already deployed

### Environment Variables in Vercel

Set in Vercel project settings:

```
NEXT_PUBLIC_API_BASE_URL=https://foundergpt-production.up.railway.app/api/v1
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_live_...  (optional, leave empty for public mode)
CLERK_SECRET_KEY=sk_live_...  (optional, server-side only)
```

### Automatic Deployment

Vercel will automatically:
1. Detect Next.js framework
2. Run `npm install`
3. Run `npm run build`
4. Deploy to `https://<project>.vercel.app`

### Configuration Files

- `next.config.ts` - Next.js configuration
- `tailwind.config.ts` - TailwindCSS theme and utilities
- `tsconfig.json` - TypeScript configuration
- `middleware.ts` - Request middleware for authentication
- `vercel.json` - Vercel deployment configuration

## Features

- **Dark Mode**: Premium dark interface with glass morphism
- **Authentication**: Clerk integration (works without Clerk keys in dev)
- **Chat**: Real-time startup idea evaluation with NVIDIA AI
- **Responsive**: Mobile-first design with TailwindCSS
- **Server Components**: React 19 Server Components where applicable
- **Type Safety**: Full TypeScript throughout

## Components

### Layout
- `app/layout.tsx` - Root layout with metadata
- `components/layout/sidebar.tsx` - Navigation sidebar
- `components/layout/auth-actions.tsx` - Login/logout UI

### Founder Dashboard
- `components/founder/dashboard-shell.tsx` - Main dashboard layout
- `components/founder/startup-chat.tsx` - Startup idea chat component
- `components/founder/project-workspace.tsx` - Project editor

### UI Components
- `components/ui/button.tsx` - Button with variants
- `components/ui/glass-card.tsx` - Glassmorphism card

## API Integration

All API calls go through `lib/api.ts` which handles:
- Base URL configuration
- Bearer token authentication
- Error handling and retry logic
- JSON serialization

### Example

```typescript
const response = await evaluateStartupIdea({
  startupIdea: "My startup idea...",
  conversationHistory: [],
  token: "dev"  // Uses NEXT_PUBLIC_DEV_API_TOKEN if not provided
});
```

## Development Tips

### Hydration Mismatches
The app uses `suppressHydrationWarning` on the HTML element to prevent Clerk-related hydration issues.

### Client Components
Use `"use client"` only for components that need interactivity. Most components are Server Components by default.

### Styling
TailwindCSS is configured with custom colors and utilities. Check `tailwind.config.ts` for the color palette.

## Troubleshooting

### Backend connection fails
1. Check `NEXT_PUBLIC_API_BASE_URL` is set correctly
2. Ensure backend is running and accessible
3. Check browser console for CORS errors

### Clerk errors on dev
Clerk is optional in development. Leave `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` empty to use dev mode without authentication.

### Build fails on Vercel
1. Check all environment variables are set
2. Ensure no hardcoded localhost URLs
3. Run `npm run typecheck` locally to catch TypeScript errors
