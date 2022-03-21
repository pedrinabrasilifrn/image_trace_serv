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
    timer = models.IntegerField("Tempo em segundos", null=False, blank= False, default= 4)
    OPTION_CHOICES = (
        ('1', 'Verde'),
        ('2', 'Vermelho')
    )
    correct_op = models.CharField("Correta", null=False, blank=False, choices=OPTION_CHOICES, default='1', max_length=1)
    wrong_op = models.CharField("Incorreta", null=False, blank=False, choices=OPTION_CHOICES, default='2', max_length=1)
    SPEED_CHOICES = (
        ('F', 'Rápido'),
        ('N', 'Normal'),
        ('S', 'Lento')
    )
    speed = models.CharField("Velocidade", choices=SPEED_CHOICES, default='N', max_length=1)
    noise = models.BooleanField("Com ruido", default= False)
    upsidedown = models.BooleanField("Invertido", default= False)
    module = models.ForeignKey(Module, verbose_name="Bloco", null=True, on_delete=models.PROTECT, related_name='resets')
  
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
    created = models.DateTimeField("Cadastrado", auto_now_add=True)
    updated = models.DateTimeField("Atualizado", auto_now=True)
    quests = models.ManyToManyField(Quest, verbose_name="Vídeos")
    class Meta:
        verbose_name = 'Experimento'
        verbose_name_plural= 'Experimentos'
        ordering = ("-created","title",)
        
    def __str__(self):
        return self.title