# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 02:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0002_auto_20161204_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('source', models.TextField(blank=True)),
                ('reference', models.TextField(blank=True)),
                ('verified', models.BooleanField(default=False)),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0, "ratings shouldn't be negative"), django.core.validators.MaxValueValidator(10, 'the maximum rating is 10')])),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.Author')),
            ],
            options={
                'verbose_name': 'Quote',
                'verbose_name_plural': 'Quotes',
            },
        ),
    ]
