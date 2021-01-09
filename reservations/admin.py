from django.contrib import admin
from .models import Reservation, BookedDay

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        'room',
        'status',
        'check_in',
        'check_out',
        'guest',
        'in_progress',
        'is_finished'
    ]

    list_filter = (
        'status',
    )

@admin.register(BookedDay)
class BookedDayAdmin(admin.ModelAdmin):

    list_display = ("day", "reservation")
