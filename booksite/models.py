from django.db import models
from django.utils import timezone


class Tale(models.Model):
    title = models.CharField(max_length=200)
    about = models.TextField(max_length=1000)
    image_path = models.CharField(max_length=200)
    pdf_path = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    downloads = models.IntegerField(default=0)

    def __str__(self):
        return self.title
