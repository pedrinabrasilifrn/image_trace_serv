# Generated by Django 4.0.2 on 2022-03-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0006_alter_module_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='noise',
            field=models.BooleanField(default=False, verbose_name='Com ruido'),
        ),
        migrations.AddField(
            model_name='quest',
            name='speed',
            field=models.IntegerField(default=1, verbose_name='Velocidade'),
        ),
        migrations.AddField(
            model_name='quest',
            name='upsidedown',
            field=models.BooleanField(default=False, verbose_name='Invertido'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='timer',
            field=models.IntegerField(default=4, verbose_name='Tempo em segundos'),
        ),
    ]