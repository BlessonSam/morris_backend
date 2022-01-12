# Generated by Django 3.2.10 on 2022-01-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morris_python', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
            ],
            options={
                'verbose_name_plural': 'Topics',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='rythm_of_english',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='teching_platform',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='aim',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='content',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='methodology',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='objective',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='section',
            field=models.TextField(null=True),
        ),
        migrations.RemoveField(
            model_name='course',
            name='topics',
        ),
        migrations.AddField(
            model_name='course',
            name='topics',
            field=models.ManyToManyField(null=True, to='morris_python.topic'),
        ),
    ]
