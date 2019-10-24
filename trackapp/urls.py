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
    path('createEnquiry/', views.fn_create_enquiry),
    path('createConsumer/', views.fn_create_consumer),
    path('createEmployee/', views.fn_create_employee),
    path('createProduct/', views.fn_create_product),
    path('delete_product/', views.fn_delete_product),
    path('delete_enquiry/', views.fn_delete_enquiry),
    path('followup', views.fn_follow_up),
    path('getNotification', views.fn_get_notifications),
    path('savefollowup/', views.fn_save_follow_up),
    path('removeFollowup/', views.fn_delete_followup),
    path('finishFollowup/', views.fn_finish_followup),
    path('changePassword/', views.fn_change_password),
    path('editenquiry/', views.fn_edit_enquiry),
    path('createLeadSource/', views.fn_create_lead_source),
    path('viewconsumer/',views.fn_view_consumer)
]
