from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    blog_image_url = models.URLField()
    description = models.TextField()
    reading_time = models.IntegerField()
    author_name = models.CharField(max_length=50)
    author_designation = models.CharField(max_length=100)
    author_image_url = models.URLField()

    def __str__(self):
        return self.title
    

