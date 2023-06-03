from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_menu = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FlashNews(models.Model):
    title = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='articles/')
    timestamp = models.DateTimeField(auto_now=True)
    description = models.TextField()
    author_image = models.ImageField(upload_to='articles/')
    author_name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    is_draft = models.BooleanField(default=True)

    @property
    def get_short_desc(self):
        return self.description[:100]

    def get_related_posts(self):
        return Article.objects.filter(tags__in=self.tags.all())[:2]
