# news/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # This pattern handles the root of the /news/ URL (e.g., http://127.0.0.1:8000/news/)
    path('', views.article_list, name='article_list'),
]