# ============================================================
# floodguard_api/urls.py
# FloodGuard ASEAN — Main URL Config
# ============================================================

from django.contrib import admin
from django.urls import path, include
from .views import serve_ionic

urlpatterns = [
    path('admin/',  admin.site.urls),
    path('api/',    include('nlp.urls')),
    # Serve Ionic app - must be last
    path('', serve_ionic),
    path('<path:path>', serve_ionic),
]