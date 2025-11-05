# profiles/urls.py
from django.urls import path
from . import views

# profiles/urls.py
# ... other imports
urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('directory/', views.faculty_directory, name='faculty_directory'), # <--- Add this line
    path('<str:username>/', views.profile_view, name='profile_detail'),
]