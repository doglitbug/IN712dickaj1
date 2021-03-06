from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    owner = models.ForeignKey('auth.User', related_name='books')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, default='')
    author = models.CharField(max_length=100)
    intro = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    url = models.URLField()
    
    class Meta:
        ordering = ('created',)
