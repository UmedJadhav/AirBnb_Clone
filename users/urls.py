from django.contrib import admin
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", views.LoginView.as_view(), name="login"),
    path('logout', views.logout, name='logout'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path("verify/<str:key>/", views.complete_verification, name="complete-verification"),
]