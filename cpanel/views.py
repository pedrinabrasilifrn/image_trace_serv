from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic import TemplateView

from .models import *

class DashboardView(TemplateView):
    template_name = "dashboard.html"

class QuestsListView(ListView):
    model = Quest

class ExperimentsListView(ListView):
    model = Experiment

class ModulesListView(DetailView):
    model = Module