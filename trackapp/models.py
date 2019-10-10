from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)


class UserRole(models.Model):
    fk_company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    role_title = models.CharField(max_length=20)


class Permission(models.Model):
    fk_role_id = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    permission_title = models.CharField(max_length=20)


class UserLogin(models.Model):
    fk_company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Consumer(models.Model):
    fk_created_user_id = models.ForeignKey(UserLogin, on_delete=models.CASCADE)
    fk_company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    fistname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)


class UserDetails(models.Model):
    fk_login_id = models.ForeignKey(UserLogin, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    dob = models.DateField()
    email = models.CharField(max_length=25)
    mobile = models.CharField(max_length=25)
    gender = models.CharField(max_length=10)


class Product(models.Model):
    fk_created_user_id = models.ForeignKey(UserLogin, on_delete=models.CASCADE)
    fk_company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=20)
    product_name = models.CharField(max_length=50)
    product_cost = models.CharField(max_length=50)
    product_desc = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(null=True, blank=True)


class Leads(models.Model):
    fk_created_user_id = models.ForeignKey(UserLogin, on_delete=models.CASCADE)
    fk_updated_user_id = models.ForeignKey(
        UserLogin, on_delete=models.CASCADE, default=None, related_name="fk_updated_user_id")
    fk_company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    fk_assigned_user_id = models.ForeignKey(
        UserLogin, on_delete=models.CASCADE, related_name="fk_assigned_user_id")
    fk_consumer_id = models.ForeignKey(
        Consumer, on_delete=models.CASCADE)
    lead_title = models.CharField(max_length=30)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    updated_date = models.DateField(null=True, blank=True)


class LeadDetails(models.Model):
    fk_lead_id = models.ForeignKey(Leads, on_delete=models.CASCADE)
    fk_product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    lead_source = models.CharField(max_length=20)
    lead_stage = models.CharField(max_length=15)


class FollowUp(models.Model):
    fk_lead_id = models.ForeignKey(Leads, on_delete=models.CASCADE)
    fk_created_user_id = models.ForeignKey(UserLogin, on_delete=models.CASCADE)
    followup_title = models.CharField(max_length=20)
    followup_description = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)


class Notification(models.Model):
    fk_company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    notification_title = models.CharField(max_length=50)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, default=None)
    object_id = models.PositiveIntegerField(default=None)
    content_object = GenericForeignKey('content_type', 'object_id')
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
