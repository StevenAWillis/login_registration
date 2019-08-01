from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):

    def registration_validator(self, postData):
            errors = {}

            email_match = User.objects.filter(email = postData['email'])
            if len(postData['email']) == 0:
                errors["email_blank"] = "Please enter your email."
            elif len(email_match) > 0:
                errors["email_invalid"] = "That email exist in the database already."

            if len(postData['first_name']) == 0:
                errors["first_name"] = "First Name field cannot be blank."
            elif postData['first_name'].isalpha() == False:
                errors["first_name_alpha"] = "First Name field must only contain letters"
            elif len(postData['first_name']) < 2:
                errors["first_name_short"] = "First Name should be at least 2 characters"

            if len(postData['last_name']) == 0:
                errors["last_name"] = "Last Name field cannot be blank."
            elif postData['last_name'].isalpha() == False:
                errors["last_name_alpha"] = "Last Name field must only contain letters"
            elif len(postData['last_name']) < 2:
                errors["last_name_short"] = "Last Name should be at least 2 characters"

            if len(postData['password']) == 0:
                errors["pword_blank"] = "Password field cannot be blank."
            elif len(postData['password']) < 8:
                errors["pword_short"] = "Password must be at least 8 characters" 

            if (postData['password'] != postData['confirm_pass']):
                errors["pword_match_fail"] = "Passwords do not match."

            return errors

    def login_validator(self, postData):
            errors = {}
            user = User.objects.filter(email = postData['email_login'])

            if len(user) == 0:
                errors["invalid"] = "Invalid login credentials."
            else:
                user = User.objects.get(email = postData['email_login'])
                if postData['password_login'] == user.password:
                    print("Password accepted, logging in...")
                
                else:
                    errors["invalid"] = "Invalid login credentials."

            return errors
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45) 
    email = models.TextField()
    password = models.TextField()
    confirm_pass = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
