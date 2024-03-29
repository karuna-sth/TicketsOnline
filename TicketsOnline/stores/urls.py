from django.urls import path

from . import views

app_name = 'stores'
urlpatterns = [
        #Leave as empty string for base url
	path('', views.index, name="index"),
	path('aboutus', views.aboutUs, name="aboutus"),
	path('event/', views.event, name="event"),
	path('checkout/', views.checkout, name="checkout"),
	path('sports/', views.sports, name="sports"),
	path('sports/bookticket', views.bookticket, name="bookticket"),
]