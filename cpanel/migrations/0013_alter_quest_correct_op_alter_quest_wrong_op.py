# Generated by Django 4.0.2 on 2022-03-21 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0012_alter_quest_speed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='correct_op',
            field=models.CharField(choices=[('1', 'Verde'), ('2', 'Vermelho')], default='1', max_length=1, verbose_name='Correta'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='wrong_op',
            field=models.CharField(choices=[('1', 'Verde'), ('2', 'Vermelho')], default='2', max_length=1, verbose_name='Incorreta'),
        ),
    ]
