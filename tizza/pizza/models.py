from django.db import models
from user.models import UserProfile


class Pizzeria(models.Model):
    name = models.CharField(max_length=120, default="")
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pizzeria'
        verbose_name_plural = 'Pizzerias'
        ordering = ['owner']



class Pizza(models.Model):
    CHOICES = (
        ('CA', 'Carne'),
        ('VE', 'Vegetariana'),
        ('VG', 'Vegana'),
        ('DC', 'Doce')
    )
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    type = models.CharField(max_length=20, choices=CHOICES, default="")
    thumbnail_url = models.URLField(default="")
    approved = models.BooleanField(default=False)
    creator = models.ForeignKey(Pizzeria, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'
        ordering = ['title']


class Likes(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
