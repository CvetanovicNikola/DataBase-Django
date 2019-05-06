from django.db import models


class Employee(models.Model):
    SEX_CHOICES = [("M", "Male"), ("F", "Female")]
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    ocupation = models.CharField(max_length=20)
    emp_id = models.IntegerField()
    description = models.TextField(null=True)
    date = models.DateTimeField(null=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    photo = models.ImageField(upload_to="emp_picture/",
                              default="static/profile_default.jpg")

    def __str__(self):
        return self.firstname
