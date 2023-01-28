# Generated by Django 3.2.4 on 2021-06-18 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/')),
                ('posted_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='GetInTouch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField(max_length=150)),
                ('sent_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/')),
                ('posted_at', models.DateField()),
                ('pre_time', models.CharField(max_length=150)),
                ('cook_time', models.CharField(max_length=150)),
                ('stars', models.IntegerField()),
            ],
        ),
    ]