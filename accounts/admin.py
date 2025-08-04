from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Appointment

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_doctor', 'is_patient', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {
            'fields': (
                'profile_pic', 'address_line1', 'city',
                'state', 'pincode', 'is_doctor', 'is_patient'
            )
        }),
    )

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'status', 'created_at')
    list_filter = ('status', 'date', 'doctor')
    search_fields = ('patient__username', 'doctor__username', 'reason')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Appointment, AppointmentAdmin)

