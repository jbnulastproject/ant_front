from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=10)
    date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]