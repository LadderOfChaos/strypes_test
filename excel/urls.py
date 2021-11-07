from django.urls import path
from .views import upload_file_view, edit_details

app_name = 'excel'

urlpatterns=[
    path('', upload_file_view, name='upload-view'),
    path('<int:pk>/edit', edit_details, name='edit-details'),
]
