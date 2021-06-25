from django.db import models

# Create your models here.
class Shool(models.Model):
    name=models.CharField( max_length=50)
    country=models.CharField( max_length=50)
    city=models.CharField( max_length=50)
    address=models.CharField( max_length=50)
    logo=models.ImageField( upload_to='images', height_field=None, width_field=None, max_length=None)
    
    class Meta:
        verbose_name = ("Shool")
        verbose_name_plural = ("Shools")

    def __str__(self):
        return self.name

 