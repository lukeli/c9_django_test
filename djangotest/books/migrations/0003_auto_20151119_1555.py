# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_author_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='title',
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(to='books.Author', default=1),
            preserve_default=False,
        ),
    ]
