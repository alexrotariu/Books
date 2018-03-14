from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, default="")
    title_slug = models.SlugField(max_length=100, default="")
    author = models.CharField(max_length=100, default="")
    author_slug = models.SlugField(max_length=100, default="")
    genre = models.CharField(max_length=100, unique=True)
    pub_year = models.IntegerField(default=0)
    summary = models.TextField(default="")
    characters = models.TextField(default="")

    def __str__(self):
        return "%s - %s" % (self.title, self.author)

