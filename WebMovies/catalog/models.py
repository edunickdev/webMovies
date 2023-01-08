from django.db import models


# Create your models here.

class Genres(models.Model):
	name = models.CharField(max_length=60, help_text='nombre del genero')
	
	def __str__(self):
		return self.name
	
	
class Nationalities(models.Model):
	country = models.CharField(max_length=30, help_text='escriba aquí el país de origen')
	
	def __str__(self):
		return self.country
	

class Directors(models.Model):
	name = models.CharField(max_length=60)
	lastName = models.CharField(max_length=60)
	year = models.CharField(max_length=4)
	nation = models.ForeignKey('Nationalities', on_delete=models.SET_NULL, null=True)
	
	def __str__(self):
		return self.name and self.lastName
	
	
class movies(models.Model):
	title = models.CharField(max_length=35)
	Genre = models.ManyToManyField(Genres)
	summary = models.TextField(max_length=150, help_text='Escribe un breve resumen', null=True)
