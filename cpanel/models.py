from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from django.conf import settings

class Module(models.Model):
    name = models.TextField("Nome",  null=True, blank=True)
    created = models.DateTimeField("Cadastrado", auto_now_add=True)
    updated = models.DateTimeField("Atualizado", auto_now=True)
    
    class Meta:
        verbose_name = 'Bloco'
        verbose_name_plural= 'Blocos'
        ordering = ("-created","name",)
        
    def __str__(self):
        return self.name


# Create your models here.
class Quest(models.Model):
    name = models.CharField("Título do Vídeo",  null=False, blank=False, max_length=100, default="Movimento do Vídeo")
    txt = models.TextField("Orientação", null=False, blank=False)
    timer = models.IntegerField("Segundos", null=False, blank= False, default= 4)
    correct_op = models.CharField("Opção Correta",  null=False, blank=False,max_length=100)
    wrong_op = models.CharField("Opção Incorreta",  null=False, blank=False, max_length=100)
    
    module = models.ForeignKey(Module, on_delete=models.PROTECT, related_name='resets')
    
    LEVEL_CHOICES = (
        ('F', 'Fácil'),
        ('N', 'Normal'),
        ('D', 'Difícil')
    )
    
    level = models.CharField("Nível de Dificuldade:", max_length=1, choices=LEVEL_CHOICES, default='F')
    
    videofile = models.FileField("Arquivo txt do vídeo", upload_to='quests/%Y/%m/%d')
 
    created = models.DateTimeField("Cadastrado", auto_now_add=True)
    updated = models.DateTimeField("Atualizado", auto_now=True)
    
    class Meta:
        verbose_name = 'Vídeo'
        verbose_name_plural= 'Vídeos'
        ordering = ("-created","name",)
        
    def __str__(self):
        return self.name

# Create your models here.
class Experiment(models.Model):
    title = models.TextField("Título",  null=False, blank=False, max_length=255)
    quests = models.ManyToManyField(Quest)
    created = models.DateTimeField("Cadastrado", auto_now_add=True)
    updated = models.DateTimeField("Atualizado", auto_now=True)
    
    class Meta:
        verbose_name = 'Experimento'
        verbose_name_plural= 'Experimentos'
        ordering = ("-created","title",)
        
    def __str__(self):
        return self.title