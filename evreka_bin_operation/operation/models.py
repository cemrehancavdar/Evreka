from django.db import models

# Create your models here.


class Bin(models.Model):
    id = models.BigAutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()


class OperationType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)


class Operation(models.Model):
    id = models.BigAutoField(primary_key=True)
    collection_frequency = models.IntegerField()
    last_collection = models.DateTimeField()
    operation_type = models.ForeignKey(OperationType, on_delete=models.CASCADE)
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
