from django.db import models


# Create your models here.

class Slider(models.Model):
    headline = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="uploads/slider")
    status = models.CharField(max_length=100, default="Active")

    def __str__(self):
        return self.headline


class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    fb_link = models.TextField()
    twitter_link = models.TextField()
    instagram_field = models.TextField()
    image = models.ImageField(upload_to="uploads/team")
    status = models.CharField(max_length=100, default="Active")

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    comment = models.TextField()
    image = models.ImageField(upload_to="uploads/testimonial")
    status = models.CharField(max_length=100, default="Active")

    def __str__(self):
        return self.name
