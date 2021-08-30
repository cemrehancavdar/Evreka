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
