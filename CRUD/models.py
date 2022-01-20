from django.db import models

# Create your models here.


class Accounts(models.Model):
    Name = models.CharField(max_length=500, null=True, blank=True)
    Email = models.EmailField(max_length=500, null=True, blank=True)
    Phone = models.CharField(max_length=500, null=True, blank=True)
    Username = models.CharField(max_length=500, null=True, blank=True)
    Password = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.Name