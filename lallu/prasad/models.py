from django.db import models

# Create your models here.
class padam(models.Model):
    name =models.CharField(max_length=20)
    desc =models.CharField(max_length=20)
    image= models.ImageField(upload_to='files/covers')

def __str__(self):
    return self.name+''+self.desc