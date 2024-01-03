# Generated by Django 5.0.1 on 2024-01-03 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('td_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='technicaldebt',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='td_app.project'),
        ),
    ]
