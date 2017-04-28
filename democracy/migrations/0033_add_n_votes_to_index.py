# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-28 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('democracy', '0032_add_language_code_to_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentimage',
            options={'ordering': ('ordering', 'title'), 'verbose_name': 'comment image', 'verbose_name_plural': 'comment images'},
        ),
        migrations.AlterField(
            model_name='sectioncomment',
            name='n_votes',
            field=models.IntegerField(db_index=True, default=0, editable=False, help_text='number of votes given to this comment', verbose_name='vote count'),
        ),
    ]
