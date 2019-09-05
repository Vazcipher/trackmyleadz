from django.db import models

# Create your models here.
class Login(models.Model):
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
	role=models.CharField(max_length=20)


class Company(models.Model):
	company_title = models.CharField(max_length=20)
	company_name = models.CharField(max_length=25)
	address = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	phn = models.CharField(max_length=25)

class Role(models.Model):  
	role_title = models.CharField(max_length=15)
	fk_company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
		
class UserDetails(models.Model):
	fk_login_id = models.ForeignKey(Login, on_delete=models.CASCADE)
	user_name = models.CharField(max_length=25)
	address = models.CharField(max_length=25)
	dob = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	mobile = models.CharField(max_length=25)
	password=models.CharField(max_length=25)

class Enquiry(models.Model):
    lead_title = models.CharField(max_length=25)
    lead_status = models.CharField(max_length=25)
    lead_source = models.CharField(max_length=25)

class Enquires(models.Model):
	enquiry_title = models.CharField(max_length=25)
	enquiry_date = models.DateField()
	description = models.CharField(max_length=50)
	phn = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	fk_emp_id = models.ForeignKey(Enquiry, on_delete=models.CASCADE)


class Employee(models.Model):
    emp_name = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    dob = models.CharField(max_length=25)
    mobile = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    fk_login_id = models.ForeignKey(Login,on_delete=models.CASCADE)

class FollowUp(models.Model):
    plan = models.CharField(max_length=25)
    date = models.CharField(max_length=25)
    time = models.CharField(max_length=25)
    remainder = models.CharField(max_length=25)
    follows = models.CharField(max_length=25)
    fk_enq_id = models.ForeignKey(Enquiry, on_delete=models.CASCADE)

class Remainder(models.Model):
	remainder = models.CharField(max_length=25)
	date = models.CharField(max_length=25)

class Sms(models.Model):
	msg = models.CharField(max_length=25)
   
class Work_Assign(models.Model):
	work_title = models.CharField(max_length=25)
	
class Notification(models.Model):
	date = models.CharField(max_length=25)
	time = models.CharField(max_length=25)
	subject = models.CharField(max_length=25)
	to = models.CharField(max_length=25)
	fromaddr = models.CharField(max_length=25)
    

