from django.db import models


class author(models.Model):
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=12)
    author=models.ForeignKey(author,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
