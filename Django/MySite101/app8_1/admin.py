from django.contrib import admin
from .models import Person

from .models import Author, Book

from .models import Publication, Article

from .models import Place, Restaurant, Waiter

# Register your models here.
admin.site.register(Person)
admin.site.register(Author)
admin.site.register(Book)

admin.site.register(Publication)
admin.site.register(Article)

admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)
