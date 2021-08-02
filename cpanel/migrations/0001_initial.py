# Generated by Django 3.2.3 on 2021-07-30 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True, verbose_name='Orientação')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado')),
            ],
            options={
                'verbose_name': 'Módulo',
                'verbose_name_plural': 'Módulos',
                'ordering': ('-created', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.TextField(verbose_name='Orientação')),
                ('timer', models.IntegerField(default=4, verbose_name='Tempo em Segundos')),
                ('correct_op', models.TextField(verbose_name='Opção Correta')),
                ('wrong_op', models.TextField(verbose_name='Opção Errada')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Volume')),
                ('videofile', models.FileField(upload_to='quests/%Y/%m/%d')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Questão',
                'verbose_name_plural': 'Questões',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255, verbose_name='Descrição')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado')),
                ('quests', models.ManyToManyField(to='cpanel.Quest')),
            ],
            options={
                'verbose_name': 'Experimento',
                'verbose_name_plural': 'Experimentos',
                'ordering': ('-created', 'title'),
            },
        ),
    ]
