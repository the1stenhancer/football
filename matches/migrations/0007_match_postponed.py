# Generated by Django 4.1 on 2022-09-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0006_remove_match_slug_match_motd'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='postponed',
            field=models.BooleanField(default=False),
        ),
    ]
