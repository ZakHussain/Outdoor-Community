from __future__ import unicode_literals
from django.db import models
import bcrypt

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.
class UserManager(models.Manager):
	def login(self,email, password):
		u = self.filter(email = email)
		if len(u)>0:
			hash=u[0].password.encode()
			password=password.encode()
			print password
			if bcrypt.hashpw(password, hash) == hash:
				message="Sucessful Login!"
				data = (
					True,
					message,
					u[0].firstName,
					u[0].lastName,
					u[0].email,
					u[0].created_at
					)
				return data
			else:
				message="Password and email must be correct for login!"
				data = (
					False,
					message
					)
				return data
		else:
			message="Password and email must not be blank to login!"
			data = (
				False,
				message
				)
			return data
	def registration(self, firstName,lastName,email,password,confirmPassword):
		print "Registration Working"
		if len(firstName)<2 or firstName.isalpha()!=True:  #isaplha()....what to import?
			message="First Name cannot be empty and must have alphabetic characters only!"
			data=(
				False,
				message
			)
			return data
		elif len(lastName)<2 or lastName.isalpha()!=True:
			message="Last Name cannot be empty and must have alphabetic characters only!"
			data=(
				False,
				message
			)
			return data
		elif not EMAIL_REGEX.match(email):
			message = "Email cannot be empty and must be proper format (user@domain.com/net/org)!"
			data = (
				False,
				message
        	   )
			return data
		elif len(password) <8:
			message="Password cannot be empty and has to be more than 8 characters long!"
			data=(
				False,
				message
			)
			return data
		elif len(confirmPassword) <8 and confirmPassword!=password:
			message = "Confirm Password cannot be empty,has to be more than 8 characters long and must match original password!"
			data=(
				False,
				message
			)
			return data
		else:
			message = "The email address you entered, "+ email +" is a VALID email address! Thank you!"
			password = password.encode()
			pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())
			e = User.objects.create(firstName=firstName, lastName=lastName,email=email,password=pw_hash)
			data = (
				True,
				message,
				e.firstName,
				e.lastName,
				e.email,
				e.created_at
        	   )
			return data
class User(models.Model):
	firstName = models.CharField(max_length = 255)
	lastName = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()
	objects = models.Manager()
