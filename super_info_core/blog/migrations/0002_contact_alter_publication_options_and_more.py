# Generated by Django 5.0.6 on 2024-08-05 13:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'verbose_name': 'Публикации', 'verbose_name_plural': 'Публикация'},
        ),
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
