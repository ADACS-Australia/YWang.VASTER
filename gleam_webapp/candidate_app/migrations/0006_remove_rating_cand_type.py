# Generated by Django 4.2 on 2024-03-08 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_app', '0005_classification_alter_candidate_filter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='cand_type',
        ),
    ]
