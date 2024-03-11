# Generated by Django 4.2 on 2024-03-11 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_app', '0006_remove_rating_cand_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='Classification'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='Project name'),
        ),
    ]
