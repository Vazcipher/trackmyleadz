from django.urls import path
from .import views

urlpatterns = [
    path('', views.indexPage),
    path('dashboard', views.home),
    path('logout', views.logoutUser),
    path('enquires', views.enquires),
    path('consumer', views.consumer),
    path('employee', views.employee),
    path('others', views.product),
    path('reports', views.reports),
    path('charts', views.charts),
    path('createEnquiry/', views.fn_create_enquiry),
    path('getEnquiry', views.fn_get_enquiry),
    path('createConsumer/', views.fn_create_consumer),
    path('createEmployee/', views.fn_create_employee)
]
