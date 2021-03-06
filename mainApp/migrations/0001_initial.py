# Generated by Django 3.2 on 2021-05-05 17:54

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
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название конференции')),
                ('organizer', models.CharField(max_length=100, verbose_name='Организатор')),
                ('description', models.TextField(verbose_name='Описание конференции')),
                ('place', models.CharField(max_length=120, verbose_name='Место проведения')),
                ('date', models.DateTimeField(verbose_name='Дата начала')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
