# Generated by Django 3.2.16 on 2023-04-18 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('name', models.CharField(max_length=256, verbose_name='Имя')),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'местоположение',
                'verbose_name_plural': 'Местоположения',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Описание')),
                ('pub_date', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='публикация', to=settings.AUTH_USER_MODEL, verbose_name='Публикации')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='категория', to='blog.category', verbose_name='Категории')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='местоположение', to='blog.location', verbose_name='Местоположения')),
            ],
            options={
                'verbose_name': 'публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
    ]
