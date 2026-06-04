# FloodGuard Deployment Guide - Option 1: Django Serves Ionic

## Architecture
```
┌─────────────────┐
│   Ionic App     │
│  (Built HTML)   │
│                 │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  Django Server  │
│  - API Routes   │
│  - Serves SPA   │
└─────────────────┘
         │
         ↓
    Database
```

## What We've Done

1. ✅ Built Ionic app with `npm run build` → Creates optimized static files
2. ✅ Updated Django settings.py:
   - Set `DEBUG = False` for production
   - Configured `STATIC_ROOT` and `STATICFILES_DIRS`
   - Pointed Django to Ionic build files
3. ✅ Updated Django urls.py to serve Ionic app
4. ✅ Created custom view for SPA routing
5. ✅ Added requirements.txt with all dependencies
6. ✅ Created Procfile for hosting platform

## Pre-Deployment Steps

### 1. Update Django Settings (IMPORTANT)

Edit [floodguard_api/floodguard_api/settings.py](floodguard_api/floodguard_api/settings.py):

```python
# Set your secret key from environment variable
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Set to False for production
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Add your domain
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'yourapp.railway.app']
```

### 2. Collect Static Files Locally (Test)

```bash
cd floodguard_api
python manage.py collectstatic --noinput
```

### 3. Test Locally

```bash
cd floodguard_api
python manage.py runserver
```

Then visit: http://localhost:8000

## Deployment to Railway (Recommended)

### Step 1: Create Railway Account
- Go to https://railway.app
- Sign up with GitHub

### Step 2: Deploy
1. Click "New Project"
2. Select "Deploy from GitHub"
3. Choose your `allainjamesybanez23/FloodGuardDeploy` repo
4. Select `floodguard_api` as the root directory

### Step 3: Environment Variables
In Railway dashboard, add these variables:

```
DEBUG=False
SECRET_KEY=your-random-secret-key-here
ALLOWED_HOSTS=yourapp.railway.app,yourdomain.com
DATABASE_URL=postgresql://... (Railway provides this)
```

To generate a SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 4: Database Migration
Railway will auto-run the Procfile:
- Install dependencies from requirements.txt
- Run migrations
- Start gunicorn server

## Update Django Settings for Database

In [floodguard_api/floodguard_api/settings.py](floodguard_api/floodguard_api/settings.py), add:

```python
import dj_database_url
import os

# Use DATABASE_URL if provided (Railway), else use SQLite
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600,
        conn_health_checks=True
    )
}
```

Then add to requirements.txt:
```
dj-database-url==1.3.0
```

## Ionic App Configuration

Make sure your Ionic app API calls use the correct backend URL:

In [floodguard_ionic/src/environments/environment.prod.ts](floodguard_ionic/src/environments/environment.prod.ts):

```typescript
export const environment = {
  production: true,
  apiUrl: 'https://yourapp.railway.app/api'
};
```

## After Deployment

1. Visit your app: https://yourapp.railway.app
2. Visit admin: https://yourapp.railway.app/admin
3. API calls go to: https://yourapp.railway.app/api/...

## Troubleshooting

**Static files not loading?**
```bash
cd floodguard_api
python manage.py collectstatic --noinput --clear
```

**API calls failing?**
- Check CORS settings in settings.py (CORS_ALLOW_ALL_ORIGINS = True is set)
- Update environment.prod.ts with correct API URL
- Check Network tab in browser dev tools

**SPA routing not working?**
- Make sure you're accessing non-API routes (not /admin/, /api/...)
- The serve_ionic view will handle routing

## Next: Update Environment Variables

Copy your current git changes:
```bash
git add .
git commit -m "Configure Django to serve Ionic app for deployment"
git push
```

Then connect Railway to your GitHub repo!
