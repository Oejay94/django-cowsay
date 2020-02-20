from django.db import models

class Cowsay(models.Model):
    text = models.TextField()