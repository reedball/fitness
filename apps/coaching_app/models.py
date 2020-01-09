from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime, timedelta, date
import math


class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors["first_name"] = "User's first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "User's last name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "User's password should be at least 8 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!")
        if postData['password_confirm'] != postData['password']:
            errors['confirm_pw'] = "Password does not match"
        return errors
    def edit_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors["first_name"] = "User's first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "User's last name should be at least 2 characters"
        # if len(postData['password']) < 8:
        #     errors["password"] = "User's password should be at least 8 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!")
        # if postData['password_confirm'] != postData['password']:
        #     errors['confirm_pw'] = "Password does not match"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()



class Goal(models.Model):
    goal_title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users_goal = models.ManyToManyField(User, related_name="goals")


class Post(models.Model):
    post_title = models.CharField(max_length=255)
    description = models.TextField()
    post_pic = models.ImageField(upload_to='images/')
    posted_by = models.ForeignKey(User, related_name="posts", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
