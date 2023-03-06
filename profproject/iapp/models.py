from django.db import models

# Create your models here.
class User(models.Model):
	Username = models.CharField(max_length=30)

class Email(models.Model):
	Email = models.EmailField()

class Password(models.Model):
	Password = models.CharField(max_length=10)

class Confirm_Password(models.Model):
	Confirm_Password = models.CharField(max_length=10)

class Address(models.Model):
	Address = models.CharField(max_length=30)

class Propic(models.Model):
	User_pic =models.ImageField(upload_to="images")
