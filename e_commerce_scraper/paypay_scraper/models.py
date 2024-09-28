from django.db import models

# Create your models here.
class product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    status=models.CharField( max_length=50)
    condition=models.CharField(max_length=50)