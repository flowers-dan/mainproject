# Generated by Django 3.0.7 on 2020-07-01 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstWEB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.CharField(max_length=10)),
                ('s_name', models.CharField(max_length=10)),
                ('s_birth', models.CharField(max_length=20)),
            ],
        ),
    ]