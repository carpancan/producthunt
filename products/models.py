from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField()
    body = models.TextField()
    published = models.DateTimeField()
    rate = models.IntegerField(default=1)
    image = models.ImageField(upload_to='products/')
    icon = models.ImageField(upload_to='products/')
    user = models.ForeignKey(User, on_delete=None)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] + '...'

    def published_pretty(self):
        return self.published.strftime('%b %e %Y')

