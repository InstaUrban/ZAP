# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amigo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('usr1', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('usr2', models.ManyToManyField(to='cuentas.Amigo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tel', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateField()),
                ('id_persona', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='datosextra',
            name='id_persona',
        ),
        migrations.DeleteModel(
            name='Datosextra',
        ),
    ]
