# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-08 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0008_categoria_posicion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyecto',
            options={'verbose_name': 'proyectos', 'verbose_name_plural': 'proyectoss'},
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='imagen',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='image',
            field=models.ImageField(default='', upload_to='proyecto', verbose_name='Imagen'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='posicion',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='cv',
            field=models.FileField(upload_to='cv', verbose_name='PDF'),
        ),
    ]
