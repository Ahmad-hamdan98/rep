from email.policy import default

from django.db import models
import re

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['firstname']) < 2:
            errors["firstname"] = "first name should be at least 2 characters"
        if len(postData['lastname']) < 2:
            errors["lastname"] = "last name should be at least 2 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):               
            errors['email'] = "Invalid email address!"
            return errors
        for u in User.objects.all():
            if postData['email'] == u.email:
                errors['email'] = "this email address! is alredy exist try another on"
                return errors

        if len(postData['pass']) < 8:
            errors["pass"] = "I dont like your password ! try again"
        if postData['confirm'] != postData['pass']:
            errors["confirm"] = " you confirm wronge passwored try again"    
        return errors

        


class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    email=models.CharField(max_length=255,default="ahmad@hamdan.com")
    password=models.CharField(max_length=255,default="password")
    confirm_PW=models.CharField(max_length=255,default="password")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()
    # addedby


class Trees(models.Model):
    specise=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    reason=models.CharField(max_length=255)
    addedby=models.ForeignKey(User ,related_name="added_by" ,on_delete=models.CASCADE)
    visetors=models.ManyToManyField(User,related_name="vistors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)