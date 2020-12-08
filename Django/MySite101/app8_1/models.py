from django.db import models

# Create your models here.

# Person is Subclass of Model Class
class Person(models.Model):
    # Fields, Class Variable
    pid = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=50)
    contact_address = models.CharField(max_length=50)
    def __str__(self):
        return str(self.pid)+", "+self.full_name+", "+self.contact_address

# Create DDL of Model - Create Statement of Table Which Map with Model
    # this process is know as mekemigrations
# Migrate newly created migrations by issuing migrate command

