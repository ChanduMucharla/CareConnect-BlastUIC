from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from datetime import date

from .forms import SignUpForm, AppointmentForm, MedicalDocumentForm
from .models import CustomUser, Appointment, Message, Notification, MedicalDocument
from .models import Message, CustomUser


# ------------------- Signup View -------------------
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# ------------------- Login View -------------------
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Invalid username or password."
    return render(request, 'login.html', {'error': error})


# ------------------- Dashboard -------------------
@login_required
def dashboard(request):
    if request.user.is_doctor:
        pending_appointments = Appointment.objects.filter(doctor=request.user, status='Pending').order_by('date', 'time')
        upcoming_appointments = Appointment.objects.filter(doctor=request.user, status='Accepted', date__gte=date.today()).order_by('date', 'time')
        previous_appointments = Appointment.objects.filter(doctor=request.user, date__lt=date.today()).order_by('-date', '-time')

        appointments = Appointment.objects.filter(doctor=request.user)

        return render(request, 'dashboard_doctor.html', {
            'appointments': appointments,
            'pending_appointments': pending_appointments,
            'upcoming_appointments': upcoming_appointments,
            'previous_appointments': previous_appointments,
        })

    elif request.user.is_patient:
        appointments = Appointment.objects.filter(patient=request.user).order_by('-date', '-time')
        return render(request, 'dashboard_patient.html', {
            'appointments': appointments
        })

    else:
        return render(request, 'unauthorized.html')


# ------------------- Book Appointment (Patient) -------------------
@login_required
def book_appointment(request):
    if not request.user.is_patient:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()

            # Notify the doctor
            Notification.objects.create(
                user=appointment.doctor,
                message=f"New appointment from {request.user.username} on {appointment.date}."
            )

            messages.success(request, "Appointment booked successfully.")
            return redirect('dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})


# ------------------- Accept Appointment (Doctor) -------------------

@login_required
def accept_appointment(request, appointment_id):
    if request.user.is_doctor:
        appointment = get_object_or_404(Appointment, id=appointment_id, doctor=request.user)
        appointment.status = "Accepted"
        appointment.save()
        Notification.objects.create(
            user=appointment.patient,
            message=f"Your appointment on {appointment.date} has been accepted by Dr. {request.user.last_name}."
        )
        messages.success(request, "Appointment accepted successfully.")
    return redirect('dashboard')



# ------------------- Chat -------------------
# accounts/views.py

@login_required
def chat_view(request, receiver_id):
    receiver = get_object_or_404(CustomUser, id=receiver_id)

    if request.method == 'POST':
        content = request.POST.get('message')
        if content:
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return redirect('chat', receiver_id=receiver.id)  # Redirect for clean POST

    messages_list = Message.objects.filter(
        Q(sender=request.user, receiver=receiver) | Q(sender=receiver, receiver=request.user)
    ).order_by('timestamp')

    return render(request, 'chat.html', {
        'receiver': receiver,
        'messages': messages_list,
        'user': request.user  # ✅ Important
    })


# ------------------- Upload Medical Documents (Patient) -------------------
@login_required
def upload_document(request):
    if not request.user.is_patient:
        return redirect('dashboard')

    if request.method == 'POST':
        form = MedicalDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.patient = request.user
            doc.save()

            # Notify all doctors (or specific one if needed)
            for doctor in CustomUser.objects.filter(is_doctor=True):
                Notification.objects.create(
                    user=doctor,
                    message=f"{request.user.username} uploaded a medical document."
                )

            messages.success(request, "Document uploaded successfully.")
            return redirect('dashboard')
    else:
        form = MedicalDocumentForm()
    
    return render(request, 'upload_document.html', {'form': form})


# ------------------- View Uploaded Documents (Doctor) -------------------
@login_required
def view_documents(request):
    if not request.user.is_doctor:
        return redirect('dashboard')

    documents = MedicalDocument.objects.all().order_by('-uploaded_at')
    return render(request, 'view_documents.html', {'documents': documents})

