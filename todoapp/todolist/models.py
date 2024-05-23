from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    PRIORITY_ORDER = {'high': 1, 'medium': 2, 'low': 3}

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название задания', max_length=500)
    created_at = models.DateField('Дата добавления')
    due_date = models.DateField('Срок выполнения')
    priority = models.CharField('Приоритет', max_length=10, choices=[('high', 'Высокий'), ('medium', 'Средний'), ('low', 'Низкий')])
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title
