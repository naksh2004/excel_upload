from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('generate_summary_report/', views.generate_summary_report, name='generate_summary_report'),  # Add this line for test upload
]
