from django.db import models

# Create your models here.
# here home is the subclass of the class Model that is made using the django library
class home(models.Model):
    firstname = models.CharField(max_length=255)

    lastname = models.CharField(max_length=255)

class information(models.Model):
    Name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    Email_id = models.CharField(max_length=255)
    address = models.CharField(max_length=255)