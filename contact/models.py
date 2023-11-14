from django.db import models
from datetime import date

class contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=True,null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField()
    date = models.DateField(default=date.today)

    
    def __str__(self):
        return self.name