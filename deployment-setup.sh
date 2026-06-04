#!/bin/bash
# deployment-setup.sh
# Prepare the app for deployment

echo "=== FloodGuard Deployment Setup ==="

# 1. Build Ionic app
echo "Building Ionic app..."
cd floodguard_ionic
npm run build
cd ..

# 2. Collect Django static files
echo "Collecting Django static files..."
cd floodguard_api
python manage.py collectstatic --noinput --clear

# 3. Create necessary files/folders
echo "Creating necessary directories..."
mkdir -p floodguard_api/staticfiles

echo "=== Setup Complete ==="
echo "Your app is ready to deploy!"
echo ""
echo "Next steps:"
echo "1. Deploy to Railway/Render with this folder"
echo "2. Set environment variables (SECRET_KEY, DEBUG=False, etc.)"
echo "3. Run migrations: python manage.py migrate"
