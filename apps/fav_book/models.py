from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

        
        

class UserManager(models.Manager):
    
    def basic_validator(self, postData):
        username = User.objects.filter(email=postData["r_email"])
        errors = {}
        if username:
            errors["r_email"] = "Email has already been registered"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if not re.match(EMAIL_REGEX, postData['r_email']):
            errors["r_email"] = "Email address not valid"
        if len(postData['r_password']) < 8:
            errors["r_password"] = "User password should be at least 8 characters"
        elif postData['r_password'] != postData['c_password']:
            errors['r_password'] = "Passswords do not match"
        return errors

    def login_validation(self,postData):
        errors ={}
        result = User.objects.filter(email=postData['l_email'])
        if result:
            if bcrypt.checkpw(postData['l_password'].encode(), result[0].password.encode()):
                print("password match")
            else:
                errors['l_password'] = "invalid login"
        else:
            errors['l_email'] = "This email has not been registered."
        return errors

class BookManager(models.Manager):
    
    def basic_validator(self, postData):
        title = Book.objects.filter(title=postData["title"])
        errors = {}
        if title:
            errors["log_email"] = "Book already been registered, check listing"
        if len(postData['title']) < 1:
            errors["title"] = "Need book title."
        if len(postData['book_desc']) < 5:
            errors["book_desc"] = "Need to know more about the book. (atleast 5 characters)"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    book_desc = models.TextField()
    upload = models.ForeignKey(User, related_name="user_upload")
    like = models.ManyToManyField(User, related_name="user_like")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()