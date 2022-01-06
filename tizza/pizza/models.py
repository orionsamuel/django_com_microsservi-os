from django.db import models

class Pizza(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'
        ordering = ['title']
