# Generated by Django 3.1.4 on 2021-06-28 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0007_auto_20210621_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='followers',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='getintouch',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='stars',
            field=models.SmallIntegerField(choices=[(1, 'One star'), (2, 'Two stars'), (3, 'Three stars'), (4, 'Four stars'), (5, 'Five stars')], default=1),
        ),
        migrations.AlterField(
            model_name='step',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
