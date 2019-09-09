from django.urls import path
from .import views

urlpatterns = [
	path('', views.indexPage),
	path('dashboard', views.home),
	path('logout', views.logoutUser)
]
