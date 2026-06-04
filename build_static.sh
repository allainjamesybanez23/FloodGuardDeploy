#!/bin/bash
# Build script for Vercel

echo "Installing dependencies..."
pip install -r floodguard_api/requirements.txt

echo "Collecting static files..."
cd floodguard_api
python manage.py collectstatic --noinput --clear --verbosity 3

echo "Build complete!"
