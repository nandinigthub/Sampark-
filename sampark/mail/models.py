
from django.shortcuts import render
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User

class Email(models.Model):
    address = models.EmailField()