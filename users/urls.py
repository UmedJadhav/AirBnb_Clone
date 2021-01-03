from django.contrib import admin
from django.urls import path

app_name = "users"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", views.LoginView.as_view(), name="login"),
]