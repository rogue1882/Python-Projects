from django.db import models


# Create your models here.

class djangoClasses(models.Model):
    Title = models.CharField(max_length=60)
    Course_Number = models.IntegerField(default="", blank=True, null=False)
    Instructor_Name = models.TextField(max_length=300)
    Duration = models.DurationField()

    objects = models.Manager()
