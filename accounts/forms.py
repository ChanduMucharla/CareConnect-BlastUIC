from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Appointment
from .models import MedicalDocument


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'profile_pic', 'is_doctor', 'is_patient',
            'address_line1', 'city', 'state', 'pincode'
        ]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        # Only show doctors in the dropdown
        self.fields['doctor'].queryset = CustomUser.objects.filter(is_doctor=True)
# forms.py
class MedicalDocumentForm(forms.ModelForm):
    class Meta:
        model = MedicalDocument
        fields = ['title', 'document']

        

