# Generated by Django 4.0.4 on 2022-06-13 20:13

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
                ('url', models.URLField(blank=True)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(default='Nrb. Kenya', max_length=80)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
