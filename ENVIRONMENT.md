# Environment Configuration Guide

## Development

### Frontend (.env.local)

```bash
cp frontend/.env.example frontend/.env.local
```

Edit `frontend/.env.local`:

```
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=
CLERK_SECRET_KEY=
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000/api/v1
NEXT_PUBLIC_DEV_API_TOKEN=dev
```

**Notes:**
- Leave `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` empty to run without Clerk
- `NEXT_PUBLIC_API_BASE_URL` points to local backend
- `NEXT_PUBLIC_DEV_API_TOKEN` is used for development requests

### Backend (.env)

```bash
cp backend/.env.example backend/.env
```

Edit `backend/.env`:

```
APP_ENV=development
FRONTEND_ORIGIN=http://localhost:3000
FRONTEND_ORIGINS=http://localhost:3000,http://localhost:3001,http://localhost:3002
NVIDIA_API_KEY=your-nvidia-api-key
DATABASE_URL=postgresql+psycopg://foundergpt:foundergpt@localhost:5432/foundergpt
```

**Notes:**
- Leave `CLERK_*` variables empty in development
- Ensure PostgreSQL is running locally

## Production

### Frontend (Vercel)

Configure in Vercel project settings → Environment Variables:

```
NEXT_PUBLIC_API_BASE_URL=https://foundergpt-production.up.railway.app/api/v1
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_live_your_key  (optional)
CLERK_SECRET_KEY=sk_live_your_key  (optional)
```

**Important:**
- `NEXT_PUBLIC_API_BASE_URL` must point to Railway backend production domain
- Clerk keys are optional - app works without them
- All `NEXT_PUBLIC_*` variables are exposed to browser

### Backend (Railway)

Configure in Railway project settings → Variables:

```
APP_ENV=production
FRONTEND_ORIGIN=https://foundergpt-x.vercel.app
FRONTEND_ORIGINS=https://foundergpt-x.vercel.app
DATABASE_URL=postgresql+psycopg://...  (Railway provides this)
NVIDIA_API_KEY=your-nvidia-api-key
CLERK_ISSUER=https://your-clerk-instance.clerk.accounts.dev
CLERK_JWKS_URL=https://your-clerk-instance.clerk.accounts.dev/.well-known/jwks.json
CLERK_AUDIENCE=your-clerk-audience
PORT=8000  (Railway sets this automatically)
```

**Important:**
- Railway automatically sets `PORT` and `DATABASE_URL`
- Ensure `FRONTEND_ORIGINS` matches Vercel deployment domain
- NVIDIA_API_KEY is required for AI features
- Clerk variables enable authentication (optional)

### Domain Configuration

**Railway Backend:**
- Domain: `foundergpt-production.up.railway.app`
- API Base: `https://foundergpt-production.up.railway.app/api/v1`
- Health: `https://foundergpt-production.up.railway.app/api/v1/health`

**Vercel Frontend:**
- Domain: `https://foundergpt-x.vercel.app` (or custom domain)
- Must have `NEXT_PUBLIC_API_BASE_URL` pointing to Railway

## Troubleshooting

### "Failed to fetch" errors in frontend
1. Check `NEXT_PUBLIC_API_BASE_URL` is set correctly
2. Verify backend is accessible from your network
3. Check CORS errors in browser console
4. Ensure backend has frontend domain in `FRONTEND_ORIGINS`

### Backend says "Clerk JWKS is not configured"
This is expected if Clerk keys are not set. The backend will reject authenticated endpoints but public endpoints work.

### "NVIDIA_API_KEY is not configured"
AI features will fail with `503 Service Unavailable`. Set `NVIDIA_API_KEY` in production.

### Database connection errors
Ensure `DATABASE_URL` is set correctly and database is accessible.

## Security Checklist

- [ ] `NVIDIA_API_KEY` is never committed to git
- [ ] Database credentials are set via environment variables
- [ ] Clerk secret keys are never in public code
- [ ] `FRONTEND_ORIGINS` is set to production domains only
- [ ] `.env` file is in `.gitignore`
- [ ] Vercel environment variables are marked as sensitive where applicable
