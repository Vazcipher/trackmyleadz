from django.urls import path
from .import views

urlpatterns = [
	path('', views.indexPage),
	path('logout', views.logoutUser)
]
