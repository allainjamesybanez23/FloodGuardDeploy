"""
Views for serving the Ionic frontend app.
"""
import os
from django.http import FileResponse
from django.conf import settings


def serve_ionic(request, path=''):
    """
    Serve the Ionic app. Falls back to index.html for SPA routing.
    """
    file_path = os.path.join(settings.STATIC_ROOT, path)
    
    # If file doesn't exist or is a directory, serve index.html (SPA routing)
    if not os.path.exists(file_path) or os.path.isdir(file_path):
        file_path = os.path.join(settings.STATIC_ROOT, 'index.html')
    
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'))
    
    # If index.html also doesn't exist, return 404
    from django.http import Http404
    raise Http404("File not found")
