# Generated by Django 5.1.4 on 2025-01-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educations_app', '0002_educationdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationdescription',
            name='description',
            field=models.TextField(max_length=512),
        ),
    ]
