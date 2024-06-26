# Generated by Django 5.0.4 on 2024-04-11 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortenedURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField()),
                ('short_url', models.CharField(max_length=8)),
            ],
        ),
        migrations.DeleteModel(
            name='URL',
        ),
    ]
