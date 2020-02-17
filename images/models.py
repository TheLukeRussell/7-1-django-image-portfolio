from django.db import models

class Image(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 30)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
