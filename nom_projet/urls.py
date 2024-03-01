from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("app1/",include("app1.urls")),
    path('admin/', admin.site.urls),
    
]
