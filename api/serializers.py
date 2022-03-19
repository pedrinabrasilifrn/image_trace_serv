from rest_framework import serializers
from django.contrib.auth.models import User
from cpanel.models import Experiment, Quest


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']

class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ['id', 'name', 'txt', 'timer', 'correct_op', 'wrong_op', 'speed', 'noise', 'upsidedown', 'videofile']

class ExperimentSerializer(serializers.ModelSerializer):
    #quests = QuestSerializer(read_only=True, many=True)
    class Meta:
        model = Experiment
        fields = ['id','title']
