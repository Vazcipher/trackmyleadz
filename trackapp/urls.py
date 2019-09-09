from django.urls import path
from .import views

urlpatterns = [
	path('', views.indexPage),
	path('dashboard', views.home),
	path('logout', views.logoutUser),
	path('enquires', views.enquires),
	path('consumer', views.consumer),
	path('employee', views.employee),
	path('others', views.others),
	path('reports', views.reports),
	path('charts', views.charts)
	
]
