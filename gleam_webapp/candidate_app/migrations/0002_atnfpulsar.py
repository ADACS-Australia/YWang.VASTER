# Generated by Django 4.2 on 2024-03-18 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ATNFPulsar',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Pulsar Name')),
                ('decj', models.FloatField(verbose_name='Declination epoch (J2000, deg)')),
                ('raj', models.FloatField(verbose_name='Right Ascension epoch (J2000, deg)')),
                ('DM', models.FloatField(verbose_name='Dispersion Measure (cm^-3 pc)')),
                ('p0', models.FloatField(verbose_name='Barycentric period of the pulsar (s)')),
                ('s400', models.FloatField(verbose_name='Mean flux density at 400 MHz (mJy)')),
            ],
        ),
    ]
