from django.db import models

# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.TextField()

"""__________________________________authentication__________________"""


    
