# Generated by Django 4.1.13 on 2024-05-04 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0013_alter_folders_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folders',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 4, 9, 50, 14, 172420, tzinfo=datetime.timezone.utc)),
        ),
    ]
