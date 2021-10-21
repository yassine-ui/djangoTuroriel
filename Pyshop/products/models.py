from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=500)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.FileField(upload_to='images',blank=True)

    #verf git
    #hi yassine


