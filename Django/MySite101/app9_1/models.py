from django.db import models

# Create your models here.


class Person(models.Model):
    full_name = models.CharField(max_length=50, help_text="NAME")
    contact_address = models.CharField(max_length=50, help_text="NAME")
    email = models.CharField(max_length=50, help_text="NAME")
    mobile = models.CharField(max_length=50, help_text="NAME")

    class Meta:
        ordering=['-id']

    def __str__(self):
        return str(self.id)+", "+self.full_name
