# Generated by Django 4.1 on 2022-09-19 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("matches", "0008_rename_motd_match_hot_pick_match_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="match",
            name="country",
            field=models.ForeignKey(
                default="AUS",
                on_delete=django.db.models.deletion.CASCADE,
                to="matches.country",
            ),
        ),
    ]