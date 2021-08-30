# Evreka Back-End Questions

Hi! This Git Repository contains answer codes of  **Evreka Back-End Developer Evaluation Questions**. As well as you can find working codes in own folders, this markdown file will highlight the piece of codes other requirements for only task related.


## Answer 1

#### Models

	from  django.db  import  models

	class  Vehicle(models.Model):
		id  = models.BigAutoField(primary_key=True)
		plate = models.CharField(max_length=200)
			
	class  NavigationRecord(models.Model):
		id  = models.BigAutoField(primary_key=True)
		vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
		datetime = models.DateTimeField()
		latitude = models.FloatField()
		longitude = models.FloatField()

#### View

	from django.http import JsonResponse
	from .models import NavigationRecord

	def index(request):
		last_navigation_records = [
			{
			"longitude": record.longitude,
			"latitude": record.latitude,
			"vehicle_plate": record.vehicle.plate,
			"datetime": record.datetime.strftime("%d.%m.%Y %H:%M:%S"),
			}
			for record in NavigationRecord.objects.distinct("vehicle").order_by(
				"vehicle", "-datetime"
			)
		]
		
		return JsonResponse({"last_points": last_navigation_records})


### Overview 

Last navigation records can get by distinct vehicle query by descending datetime order. 

### Suggestion
Timeseries data can have poor performance on standart databases when data is getting bigger but TimescaleDB and InfluxDB like time series oriented databases solves scalability.

These 2 topics focuses on exact problem: 

[# Continuous Aggregates](https://docs.timescale.com/timescaledb/latest/how-to-guides/continuous-aggregates/#continuous-aggregates)

[# Faster Distinct Queries ](https://blog.timescale.com/blog/how-we-made-distinct-queries-up-to-8000x-faster-on-postgresql/)

##### TODO

## Answer 2



#### Models
	from django.db import models

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

![model](url_here)

#### View

	from django.http import JsonResponse
	from .models import Operation


	def index(request):

		bin_operation_pair = [
			{
				"bin": record.bin.id,
				"operation": record.operation_type.name,
				"collection_frequency": record.collection_frequency,
			}
			for record in Operation.objects.all()
		]

		return JsonResponse({"last_points": bin_operation_pair})



### Overview 

Model is prepeared for different operations.