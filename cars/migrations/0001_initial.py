# Generated by Django 5.1.2 on 2024-11-08 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'olkeler',
            },
        ),
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=255, unique=True, verbose_name='NV-in barkodu')),
                ('car_nummber', models.CharField(max_length=255, verbose_name='Masin nomresi')),
                ('name', models.CharField(max_length=255, verbose_name='Adi')),
                ('weight_at_border', models.FloatField(verbose_name='Serhedeki Cekisi')),
                ('weight_at_silkway', models.FloatField(verbose_name='Ipek yolundaki cekisi')),
                ('note', models.TextField(null=True, verbose_name='Elave qeyd')),
                ('is_food', models.IntegerField(choices=[(1, 'Qida'), (2, 'Qeyri-qida')], default=1, verbose_name='Qida/qeyri-qida')),
                ('terminal', models.IntegerField(choices=[(1, 'Sederek G/P'), (2, 'Ipek G/P')], default=1)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.country', verbose_name='Olke')),
            ],
            options={
                'verbose_name_plural': 'Masinlar',
            },
        ),
    ]