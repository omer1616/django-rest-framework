from django.db import models
#Create your models here.

class Article(models.Model):
    author = models.CharField(max_length=150)
    title =  models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    text = models.TextField()
    city= models.CharField(max_length=120)
    publication_date = models.DateField()
    status= models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title