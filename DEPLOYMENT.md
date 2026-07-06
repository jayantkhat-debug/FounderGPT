# Production Deployment Checklist

## Pre-Deployment

### Code Quality
- [ ] `npm run typecheck` passes in frontend
- [ ] `npm run build` completes successfully
- [ ] `python -m compileall backend/app` has no errors
- [ ] No hardcoded localhost URLs in code
- [ ] No secrets committed to git
- [ ] No unused imports or dead code

### Configuration
- [ ] `.env.example` files are updated with all required variables
- [ ] Middleware.ts exists and is correctly configured
- [ ] CORS origins include production domains
- [ ] Backend can bind to 0.0.0.0 and custom PORT
- [ ] Procfile exists for Railway deployment

### Testing
- [ ] Backend health endpoint works: `GET /api/v1/health`
- [ ] Startup idea chat endpoint exists: `POST /api/v1/chat/startup-idea`
- [ ] Frontend loads without console errors
- [ ] No hydration mismatch warnings
- [ ] API client correctly handles errors

## Railway Backend Deployment

### Prerequisites
- [ ] GitHub repository is public or Railway has access
- [ ] PostgreSQL database provisioned (Railway add-on or external)
- [ ] NVIDIA Build API key obtained and ready

### Configuration
- [ ] Create Railway project
- [ ] Connect GitHub repository
- [ ] Add PostgreSQL plugin (optional if using external database)
- [ ] Set environment variables:
  - [ ] `APP_ENV=production`
  - [ ] `DATABASE_URL` (Railway provides if using plugin)
  - [ ] `NVIDIA_API_KEY`
  - [ ] `FRONTEND_ORIGIN` = Vercel domain
  - [ ] `FRONTEND_ORIGINS` = Vercel domain
- [ ] Set custom domain (optional)
- [ ] Configure health check: `/api/v1/health`

### Deployment
- [ ] Push code to GitHub
- [ ] Railway automatically builds and deploys
- [ ] Health check passes: `https://foundergpt-production.up.railway.app/api/v1/health`
- [ ] API docs available: `https://foundergpt-production.up.railway.app/docs` (dev only)
- [ ] Test startup chat endpoint works

### Verification
```bash
curl https://foundergpt-production.up.railway.app/api/v1/health
# Expected: {"status":"ok","service":"foundergpt-x-api"}
```

## Vercel Frontend Deployment

### Prerequisites
- [ ] GitHub repository connected to Vercel
- [ ] Railway backend URL known and accessible
- [ ] Clerk keys obtained (optional)

### Configuration
- [ ] Create Vercel project from GitHub
- [ ] Set environment variables:
  - [ ] `NEXT_PUBLIC_API_BASE_URL=https://foundergpt-production.up.railway.app/api/v1`
  - [ ] `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` (optional)
  - [ ] `CLERK_SECRET_KEY` (optional)
- [ ] Build command: `npm run build` (automatic)
- [ ] Output directory: `.next` (automatic)
- [ ] Install command: `npm install` (automatic)

### Deployment
- [ ] Push code to GitHub
- [ ] Vercel automatically builds and deploys
- [ ] Preview deployment passes all checks
- [ ] Production deployment is live
- [ ] SSL certificate is valid

### Verification
```bash
curl https://foundergpt-x.vercel.app
# Should return HTML, no errors
```

## Integration Testing

### Test Flow
1. [ ] Open frontend in browser: `https://foundergpt-x.vercel.app`
2. [ ] Dashboard loads without errors
3. [ ] No console errors or warnings
4. [ ] Sidebar items are visible
5. [ ] Enter a startup idea in chat
6. [ ] Submit chat request
7. [ ] NVIDIA API responds with evaluation
8. [ ] Response appears in chat
9. [ ] No "Failed to fetch" errors

### Error Scenarios
- [ ] Test with invalid/empty startup idea
- [ ] Test with very long input
- [ ] Check error messages are helpful
- [ ] Verify retry works on network failure

## Post-Deployment

### Monitoring
- [ ] Set up error tracking (Sentry recommended)
- [ ] Set up logging aggregation
- [ ] Configure Railway alerts for downtime
- [ ] Configure Vercel alerts for build failures

### Performance
- [ ] Check Vercel Analytics for Core Web Vitals
- [ ] Check Railway logs for API latency
- [ ] Monitor NVIDIA API response times
- [ ] Verify database query performance

### Security
- [ ] Verify HTTPS is enforced everywhere
- [ ] Check CORS headers are correct
- [ ] Ensure no sensitive data in error messages
- [ ] Review authentication flow
- [ ] Check rate limiting if needed

## Rollback Plan

### If Backend Fails
1. Roll back GitHub commit
2. Railway auto-deploys previous version
3. Check health endpoint: `https://foundergpt-production.up.railway.app/api/v1/health`

### If Frontend Fails
1. Roll back GitHub commit
2. Vercel auto-deploys previous version
3. Check frontend loads: `https://foundergpt-x.vercel.app`

### If Integration Fails
1. Check CORS headers: `Access-Control-Allow-Origin`
2. Verify `NEXT_PUBLIC_API_BASE_URL` in Vercel
3. Check database connectivity
4. Check NVIDIA API key and rate limits
5. Review logs in Railway and Vercel dashboards
