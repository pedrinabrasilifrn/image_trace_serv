from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from cpanel.models import Experiment, Quest
from api.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSets define the view behavior.
class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    
    @action(detail=True)
    def quests(self, request, pk=None):
        queryset = Experiment.objects.all()
        exp = get_object_or_404(queryset,pk=pk)
        serializer  = QuestSerializer(exp.quests, read_only=True, many=True)
        return Response(serializer.data) 


# ViewSets define the view behavior.
class QuestViewSet(viewsets.ModelViewSet):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer

