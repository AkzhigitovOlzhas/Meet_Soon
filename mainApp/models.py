from django.db import models
from django.contrib import auth


class Conference(models.Model):
    admin = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField('Название конференции', max_length=100)
    organizer = models.CharField('Организатор', max_length=100)
    description = models.TextField('Описание конференции')
    place = models.CharField('Место проведения', max_length=120)
    date = models.DateTimeField('Дата начала')


class Member(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    phone = models.CharField('Номер телефона', max_length=20)
    email = models.CharField('Почта', max_length=50)
    invitation_code = models.CharField('Код приглашения', max_length=10)
