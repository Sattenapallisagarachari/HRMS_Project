from django.db import models

class ParkingSlot(models.Model):
    is_occupied = models.BooleanField(default= False)

    def __str__(self):
        return f"slot {'occupied' if self.is_occupied else 'Available'}"