from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return "Inventory: %s" % self.name

class Computer(models.Model):
    inventory = models.ForeignKey(Inventory)
    manufacturer = models.CharField(max_length = 128)
    serial_number = models.CharField(max_length = 128)
    comments = models.TextField()

    def __str__(self):
        return "Computer: %s : %s" % (self.manufacturer, self.serial_number)

