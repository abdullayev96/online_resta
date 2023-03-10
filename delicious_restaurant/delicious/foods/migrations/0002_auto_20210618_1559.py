# Generated by Django 3.2.4 on 2021-06-18 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/')),
                ('prep_time', models.CharField(max_length=150)),
                ('cook_time', models.CharField(max_length=150)),
                ('stars', models.SmallIntegerField(choices=[(1, 'One star'), (2, 'Two stars'), (3, 'Three stars'), (4, 'four stars'), (5, 'five stars')], default=1)),
                ('posted_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('order', models.IntegerField()),
                ('recipe', models.ForeignKey(max_length=150, null=True, on_delete=django.db.models.deletion.SET_NULL, to='foods.recipe')),
            ],
        ),
        migrations.DeleteModel(
            name='Receipe',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(max_length=150, null=True, on_delete=django.db.models.deletion.SET_NULL, to='foods.recipe'),
        ),
    ]
