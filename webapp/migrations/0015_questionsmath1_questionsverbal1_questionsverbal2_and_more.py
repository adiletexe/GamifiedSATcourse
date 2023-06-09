# Generated by Django 4.1.7 on 2023-03-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_userprofile_numberoftest'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionsMath1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True)),
                ('paragraph', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('question', models.CharField(max_length=500, null=True)),
                ('answer1', models.CharField(max_length=200, null=True)),
                ('answer2', models.CharField(max_length=200, null=True)),
                ('answer3', models.CharField(max_length=200, null=True)),
                ('answer4', models.CharField(max_length=200, null=True)),
                ('correct', models.CharField(max_length=2)),
                ('explanation', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsVerbal1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True)),
                ('paragraph', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('question', models.CharField(max_length=500, null=True)),
                ('answer1', models.CharField(max_length=200, null=True)),
                ('answer2', models.CharField(max_length=200, null=True)),
                ('answer3', models.CharField(max_length=200, null=True)),
                ('answer4', models.CharField(max_length=200, null=True)),
                ('correct', models.CharField(max_length=2)),
                ('explanation', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsVerbal2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True)),
                ('paragraph', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('question', models.CharField(max_length=500, null=True)),
                ('answer1', models.CharField(max_length=200, null=True)),
                ('answer2', models.CharField(max_length=200, null=True)),
                ('answer3', models.CharField(max_length=200, null=True)),
                ('answer4', models.CharField(max_length=200, null=True)),
                ('correct', models.CharField(max_length=2)),
                ('explanation', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsVerbal3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True)),
                ('paragraph', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('question', models.CharField(max_length=500, null=True)),
                ('answer1', models.CharField(max_length=200, null=True)),
                ('answer2', models.CharField(max_length=200, null=True)),
                ('answer3', models.CharField(max_length=200, null=True)),
                ('answer4', models.CharField(max_length=200, null=True)),
                ('correct', models.CharField(max_length=2)),
                ('explanation', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='noavatar.jpg', upload_to='profile_pictures'),
        ),
    ]
