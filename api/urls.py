from django.urls import path, include
from django.contrib.auth.models import User
from cpanel.models import Experiment, Quest
from rest_framework import routers, serializers, viewsets
from api.views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'experimentos', ExperimentViewSet)
router.register(r'quests', QuestViewSet)

app_name = "api"

urlpatterns = [
    path('', include(router.urls)),
]