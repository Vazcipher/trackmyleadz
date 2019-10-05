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
    path('createConsumer/', views.fn_create_consumer),
    path('createEmployee/', views.fn_create_employee),
    path('createProduct/', views.fn_create_product),
    path('delete_product/', views.fn_delete_product),
    path('delete_enquiry/', views.fn_delete_enquiry),
    path('followup', views.fn_follow_up),
    path('getNotification', views.fn_get_notifications),
    path('savefollowup/', views.fn_save_follow_up)
]
