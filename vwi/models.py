from django.db import models

# contactUs form model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    note = models.CharField(max_length=500)

    def __str__(self):
        return self.name

#event model
class Event(models.Model):
    testname = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=False)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.testname

#alumni model   
class Alumni(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    company = models.CharField(max_length=200)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    