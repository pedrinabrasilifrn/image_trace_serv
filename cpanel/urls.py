from django.urls import path
from . import views

app_name = "cpanel"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index")
]