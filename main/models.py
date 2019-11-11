from django.db import models


class Article(models.Model):
    url = models.URLField(editable=False)
    title = models.TextField()
    content = models.TextField()
    date = models.CharField(max_length=100)
