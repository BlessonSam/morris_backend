# Generated by Django 3.2.10 on 2022-02-21 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morris_python', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='content',
        ),
        migrations.AlterField(
            model_name='course',
            name='aim',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='intro',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='methodology',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='objective',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='rythm_of_english',
            field=models.TextField(null=True),
        ),
        migrations.RemoveField(
            model_name='course',
            name='topics',
        ),
        migrations.AddField(
            model_name='course',
            name='topics',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='topic',
        ),
    ]
