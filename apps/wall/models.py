from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if not re.match(EMAIL_REGEX, postData['email']):
            errors["r_email"] = "Email address not valid"
        if len(postData['password']) < 8:
            errors["r_password"] = "User password should be at least 8 characters"
        elif postData['password'] != postData['c_password']:
            errors['password'] = "Passswords do not match"
        return errors



    def login_validation(self,postData):
        errors ={}
        result = User.objects.filter(email=postData['email'])

        if result:
            if bcrypt.checkpw(postData['password'].encode(), result[0].password.encode()):
                print("password match")
            else:
                errors['password'] = "invalid login"
        else:
            errors['email'] = "This email has not been registered."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="message")


class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="comment")
    message = models.ForeignKey(Message, related_name="comment")