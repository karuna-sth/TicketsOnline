from django.urls import path

from . import views

app_name = 'holiday'

urlpatterns = [ 
    path("", views.holiday, name="holiday"),
]