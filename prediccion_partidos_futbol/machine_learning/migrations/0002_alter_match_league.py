# Generated by Django 4.0.4 on 2022-07-02 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_learning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='league',
            field=models.CharField(choices=[('ESP', 'ESP'), ('IT', 'IT'), ('GER', 'GER'), ('FR', 'FR'), ('ENG', 'ENG')], max_length=10),
        ),
    ]
