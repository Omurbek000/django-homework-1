from django.db import models

class Event(models.Model):
     title = models.CharField('Название события',max_length=200)
     description = models.TextField('Описание события',)
     event_date = models.DateTimeField('Дата проведения события.',)
     location = models.CharField('Местоположение события',max_length=300)
     
     def __str__(self):
      return self.title
    
