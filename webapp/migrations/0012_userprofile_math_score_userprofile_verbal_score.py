# Generated by Django 4.1.7 on 2023-03-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_userprofile_tokens'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='math_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='verbal_score',
            field=models.IntegerField(null=True),
        ),
    ]