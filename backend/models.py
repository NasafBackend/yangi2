from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=50)
    matn_mazmuni=models.TextField()
    slug=models.SlugField(max_length=50)

    def __str__ (self):
         return self.slug
   