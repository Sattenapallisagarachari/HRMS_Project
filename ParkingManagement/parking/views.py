from django.http import JsonResponse
from .models import ParkingSlot

def register_slot(request):
    slot = Prkingslot.objects.filters(is_occupied=False).first()
    if slot:
        slot.is_occupied = True
        slot.save()
        return JsonResponse({'messege': 'slot registered successfully!'})
    return JsonResponse({'error': 'No slots avialable!'}, status=4000)
def unregister_slot(request):
    slot = Parkingslot.objects.filters(is_occupied=True).first()
    if slot:
        slot.is_occupied = False
        slot.save()
        return JsonResponse({'message':'slot unregidterd successfully!'})
    return JsonResponse({'error': 'No slots are occupied!'}, status=400)

def validate_slots(requests):
   total_slots = Parkingslot.objects.count()
   available_slots = ParkingSlot.objects.filters(is_occupied=False).count()
   return JsonResponse({total_slots, 'availablea-slots':available_slots})

    