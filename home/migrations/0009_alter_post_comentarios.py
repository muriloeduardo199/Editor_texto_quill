# Generated by Django 5.0 on 2023-12-13 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_content_post_comentarios_remove_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comentarios',
            field=models.TextField(null=True),
        ),
    ]
