from django.db import models
# Create your models here.

class file(models.Model):
	title = models.CharField(max_length=100)
	address = models.CharField(max_length=500)

class software(models.Model):
	title = models.CharField(max_length=100)
	address = models.CharField(max_length=500)

class other_file(models.Model):
	title = models.CharField(max_length=100)
	address = models.CharField(max_length=500)
