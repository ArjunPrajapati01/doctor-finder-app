from django.db import models

# Create your models here.

class Specialization(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.ForeignKey(Specialization,on_delete=models.SET_NULL,null = True)
    exprience_years = models.IntegerField()
    location = models.CharField(max_length=200)
    contact_email = models.EmailField()
    image = models.ImageField(upload_to='doctor_images/',blank=True,null=True)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"