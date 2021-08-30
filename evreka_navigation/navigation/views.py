from django.http import JsonResponse
from .models import NavigationRecord, Vehicle


# def index(request):

#     last_navigation_records = [
#         {
#             "longitude": record.longitude,
#             "latitude": record.latitude,
#             "vehicle_plate": record.vehicle.plate,
#             "datetime": record.datetime.strftime("%d.%m.%Y %H:%M:%S"),
#         }
#         for record in NavigationRecord.objects.distinct("vehicle").order_by(
#             "vehicle", "-datetime"
#         )
#     ]

#     return JsonResponse({"last_points": last_navigation_records})

from django.utils import timezone
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

    nav_rec_list = []


    for record in Vehicle.objects.all():
        now = timezone.now()
        for i in range(10000):
            now += timezone.timedelta(seconds=(1*i))
            nav_rec_list.append(NavigationRecord(vehicle=record, datetime =now, latitude = 33, longitude = 33.3 ))
    NavigationRecord.objects.bulk_create(nav_rec_list)
    

    return JsonResponse({"last_points": last_navigation_records})
