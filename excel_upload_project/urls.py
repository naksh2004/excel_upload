from django.contrib import admin
from django.urls import path, include  # Add include import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('excel_upload.urls')),  # Add this line to include urls from excel_upload app
]
