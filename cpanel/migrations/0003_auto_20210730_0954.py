# Generated by Django 3.2.3 on 2021-07-30 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0002_auto_20210730_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resets', to='cpanel.module'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ordem'),
        ),
    ]