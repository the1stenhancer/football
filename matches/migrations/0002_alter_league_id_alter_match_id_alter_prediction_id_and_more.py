# Generated by Django 4.1 on 2022-08-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='id',
            field=models.AutoField(help_text='uniquely identifies leagues within a country', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='match',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='result',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
