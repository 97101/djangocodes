# project_6/urls.py

from django.contrib import admin
from django.urls import path, include
from first_app import views as first_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first_views.home, name='home'),  # This assumes 'home' is defined in first_app/views.py
    path('first/', include('first_app.urls')),
]
