# Generated by Django 3.0.8 on 2020-09-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lineo', models.CharField(max_length=100)),
                ('linet', models.CharField(max_length=100)),
                ('lineth', models.CharField(max_length=100)),
            ],
        ),
    ]
