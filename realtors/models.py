from django.db import models
from datetime import datetime
# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField( upload_to='photos/%y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    # What will be displaed
    def __str__(self):
        return self.name