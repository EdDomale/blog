from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Article(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    content = models.TextField()
    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
