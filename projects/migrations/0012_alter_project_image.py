# Generated by Django 5.1.6 on 2025-04-23 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='projects/images'),
        ),
    ]
