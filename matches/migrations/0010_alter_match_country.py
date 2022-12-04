# Generated by Django 4.1 on 2022-09-19 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("matches", "0009_alter_match_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="match",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="matches.country"
            ),
        ),
    ]
