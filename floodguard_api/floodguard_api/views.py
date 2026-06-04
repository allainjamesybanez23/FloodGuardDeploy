"""
Views for serving the Ionic frontend app.
"""
import os
from django.http import FileResponse, HttpResponse
from django.conf import settings


def serve_ionic(request, path=''):
    """
    Serve the Ionic app. Falls back to index.html for SPA routing.
    """
    # Debug: log what we're trying to serve
    print(f"Trying to serve: {path}")
    print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
    print(f"STATIC_ROOT exists: {os.path.exists(settings.STATIC_ROOT)}")
    
    # Try the requested file first
    if path:
        file_path = os.path.join(settings.STATIC_ROOT, path)
        if os.path.exists(file_path) and not os.path.isdir(file_path):
            try:
                return FileResponse(open(file_path, 'rb'))
            except:
                pass
    
    # Fall back to index.html for SPA routing
    index_path = os.path.join(settings.STATIC_ROOT, 'index.html')
    if os.path.exists(index_path):
        try:
            return FileResponse(open(index_path, 'rb'))
        except Exception as e:
            return HttpResponse(f"Error serving index.html: {str(e)}", status=500)
    
    # If index.html doesn't exist, return error
    return HttpResponse("Static files not found. Please run collectstatic.", status=500)

