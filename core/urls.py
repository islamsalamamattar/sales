from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path("", include("authentication.urls")), # Auth routes - login / register
]
