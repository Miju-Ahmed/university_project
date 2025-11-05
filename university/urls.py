# university/urls.py

"""
URL configuration for the university project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import views from your apps
from core.views import homepage, about_us
from profiles import views as profile_views

urlpatterns = [
    # Admin Site
    path('admin/', admin.site.urls),

    # Core App URLs
    path('', homepage, name='homepage'),
    path('about/', about_us, name='about'),
    
    # Other App URLs
    path('courses/', include('courses.urls')),
    path('news/', include('news.urls')),
    path('events/', include('events.urls')),
    
    # Profile and Authentication URLs
    path('profile/', include('profiles.urls')),
    path('register/', profile_views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')), # Includes login, logout, etc.
]


# --- Static and Media File Serving (for Development ONLY) ---
# This pattern allows the development server to serve static and media files.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)