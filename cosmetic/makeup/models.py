from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=25)
    kind = models.CharField(max_length=25)
    descreption = models.CharField(max_length=25)
    expir_date = models.DateField()
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return super().__str__()
    
    # def get_absolute_url():
    #     pass


class Brand(models.Model):
    name = models.CharField(max_length=25)
    orgin = models.CharField(max_length=25)

    def __str__(self) -> str:
        return super().__str__()
    
    # def get_absolute_url():
    #     pass