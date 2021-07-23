from django.db import models

#СТВОРЕННЯ БАЗИДАНИХ
#СТВОРЕННЯ ТАБЛИЦІ
#ФАЙЛИ МІГРАЦІЇ ОПИСУЮТЬ ТАБЛИЦЮ ЩО СТВОРЮЄТЬСЯ КОМАНАДА(python manage.py makemigrations python manage.py migrate)
class Customers(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Message = models.TextField()

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name ='Customer'
        verbose_name_plural = 'Customers'

