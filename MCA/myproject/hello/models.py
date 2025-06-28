from django.db import models
class Faculty(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=30)
    course= models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    def __str__(self):
        return self.name

# Create your models here.
