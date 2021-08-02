from django.urls import path
from . import views

app_name = "cpanel"

urlpatterns = [
    path('', views.DashboardView.as_view(), name="dashboard"),
    path('quests', views.QuestsListView.as_view(), name="questoes"),
    path('experiments', views.ExperimentsListView.as_view(), name="experimentos"),
    path('modules', views.ModulesListView.as_view(), name="módulos"),
]