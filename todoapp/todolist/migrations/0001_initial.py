# Generated by Django 5.0.6 on 2024-05-23 09:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Название задания')),
                ('created_at', models.DateField(verbose_name='Дата добавления')),
                ('due_date', models.DateField(verbose_name='Срок выполнения')),
                ('priority', models.CharField(choices=[('high', 'Высокий'), ('medium', 'Средний'), ('low', 'Низкий')], max_length=10, verbose_name='Приоритет')),
                ('is_complete', models.BooleanField(default=False, verbose_name='Завершено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
    ]
