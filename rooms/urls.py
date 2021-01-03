from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path("search/", views.SearchView.as_view(), name="search"),
   ]