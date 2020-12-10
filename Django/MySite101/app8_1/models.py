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

# One to One Relationship
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True,)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)

# One to Many Relationship
class Author(models.Model):
    # if primary key field is not defined in model; django automatically create id as primary key
    full_name = models.CharField(max_length=50, help_text="NAME")

    def __str__(self):
        return str(self.id)+", "+self.full_name

class Book(models.Model):
    title = models.CharField(max_length=50, help_text="Book Title")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateField()

    def __str__(self):
        return str(self.id)+", "+self.title+", "+str(self.publish_date)

# One-to-Many Relationship (PrimaryKey, ForeignKey)

# Many to Many Relationship
class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline