from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=25)
    body=models.CharField(max_length=500)
    #this fun make the self title that we postet
    def __str__(self):
        return f"{self.title}"