from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('accept/<int:appointment_id>/', views.accept_appointment, name='accept_appointment'),
    path('chat/<int:receiver_id>/', views.chat_view, name='chat'),
    path('upload-document/', views.upload_document, name='upload_document'),
    path('view-documents/', views.view_documents, name='view_documents'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

