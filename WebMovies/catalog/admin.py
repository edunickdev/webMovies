from django.contrib import admin

# Register your models here.

from .models import Directors, Genres, Nationalities, movies

admin.site.register(Directors)
admin.site.register(Genres)
admin.site.register(Nationalities)
admin.site.register(movies)
