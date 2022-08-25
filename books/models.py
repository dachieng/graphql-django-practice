from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=500)

    def __str__(self):
        return self.title