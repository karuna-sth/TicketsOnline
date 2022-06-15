from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.index, name="index"),
	path('aboutus', views.aboutUs, name="aboutus"),
	path('event/', views.event, name="event"),
	path('checkout/', views.checkout, name="checkout"),
<<<<<<< HEAD
	path('sports/', views.sports, name="sports"),
	path('sports/football', views.football, name="football"),
	path('sports/bookticket', views.bookticket, name="bookticket")
=======
	path('sports', views.sports, name="sports"),
	path('register', views.register, name="register"),
>>>>>>> 440dcce667b84d3f51988692eba65f2b830a7a2c

]