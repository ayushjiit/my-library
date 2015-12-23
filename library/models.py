from django.db import models
from django.utils import timezone


class lib(models.Model):
    author = models.ForeignKey('auth.User')
    section = models.CharField(max_length=200, null = 'true')
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200,default='')
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
