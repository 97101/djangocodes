from django.db import models
from author.models import author

class Post(models.Model):
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=12)
    author=models.ForeignKey(author,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
