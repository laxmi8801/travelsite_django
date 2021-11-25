from django.db import models

# Create your models here.
class Destination:
    id: int
    name: str
    img: str
    desc: str
    price: int

class book(models.Model):
    From = models.CharField(max_length=20)
    To = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    Start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name