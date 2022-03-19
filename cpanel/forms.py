from django import forms
from django.contrib import admin
from .models import *
from django.contrib.admin.widgets import FilteredSelectMultiple
class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        exclude = []
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Digite o nome do módulo','minlength': 3, 'maxlength': 255}),
        }

class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        exclude = []
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Descreva o movimento do vídeo','minlength': 3, 'maxlength': 255}),
            'txt': forms.Textarea(attrs={'rows':4, 'cols':100}),
        }


class ExperimentForm(forms.ModelForm):
    quests = forms.ModelMultipleChoiceField(queryset=Quest.objects.all(),
                                       widget=FilteredSelectMultiple('Vídeos', False),
                                       required=False)
    class Meta:
        model = Experiment
        exclude = []
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Digite o título do experimento', 'maxlength': 255}),
            
        }