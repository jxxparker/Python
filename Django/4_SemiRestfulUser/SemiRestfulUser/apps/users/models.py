# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class userManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "First name needs to be filled in"
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last name needs to be filled in"
        if len(postData['email']) < 1:
            errors["email"] = "Email needs to be filled in"
        return errors

#create models here

class users(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()

    def __repr__(self):
        return "<users object: F_name: {}, L_name: {}, email: {}".format(self.first_name, self.last_name, self.email)