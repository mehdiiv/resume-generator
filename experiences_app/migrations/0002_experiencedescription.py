# Generated by Django 5.1.4 on 2025-01-12 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1024, unique=True)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience_descriptions', to='experiences_app.experience')),
            ],
            options={
                'db_table': 'experience_descriptions',
            },
        ),
    ]
