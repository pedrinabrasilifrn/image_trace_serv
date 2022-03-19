from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("id","name",  "created", "updated")
    exclude = []
    form = ModuleForm

@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ("id", "name","txt", "created", "updated")
    exclude = []
    form = QuestForm  

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created", "updated")
    exclude = []
    form = ExperimentForm
    