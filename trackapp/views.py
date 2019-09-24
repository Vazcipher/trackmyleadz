from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def indexPage(request):
    try:
        if request.method == 'POST':
            uname = request.POST.get('uname')
            upass = request.POST.get('password')
            user_obj = UserLogin.objects.get(username=uname, password=upass)
            request.session['userId'] = user_obj.id
            request.session['userRoleId'] = user_obj.role.id
            request.session['companyId'] = user_obj.fk_company_id.id
            return HttpResponseRedirect('dashboard')
        return render(request, 'index.html')
    except Exception as identifier:
        print(identifier)
        return render(request, 'index.html', {'msg': 'login failed'})


def home(request):
    try:
        if 'userId' in request.session:
            if 'userRoleId' in request.session:
                if 'companyId' in request.session:
                    user_obj = UserLogin.objects.get(
                        id=request.session['userId'])
                    context = {
                        "username": user_obj.username
                    }
                    return render(request, 'home.html', context)
                return redirect('/trackapp')
            return redirect('/trackapp')
        return redirect('/trackapp')
    except Exception as identifier:
        print(identifier)


def logoutUser(request):
    try:
        if 'userId' in request.session:
            del request.session['userId']
        if 'userRoleId' in request.session:
            del request.session['userRoleId']
        if 'companyId' in request.session:
            del request.session['companyId']
        return redirect('/trackapp')
    except Exception as identifier:
        print(identifier)
        return redirect('/trackapp')


def enquires(request):
    try:
        user_obj = UserLogin.objects.get(id=request.session['userId'])
        company_obj = Company.objects.get(id=request.session['companyId'])
        consumer_obj = Consumer.objects.filter(fk_company_id=company_obj)
        emp_obj = UserLogin.objects.filter(fk_company_id=company_obj)
        context = {
            "username": user_obj.username,
            "consumer_obj": consumer_obj,
            "emp_obj": emp_obj
        }
        return render(request, 'enquires.html', context)
    except Exception:
        return HttpResponse('an error occurred')


def consumer(request):
    try:
        user_obj = UserLogin.objects.get(id=request.session['userId'])
        context = {
            "username": user_obj.username
        }
        return render(request, 'consumer.html', context)
    except Exception:
        return HttpResponse('an error occurred')


def employee(request):
    try:
        user_obj = UserLogin.objects.get(id=request.session['userId'])
        company_obj = Company.objects.get(id=request.session['companyId'])
        role_obj = UserRole.objects.filter(fk_company_id=company_obj)
        context = {
            "username": user_obj.username,
            "roles": role_obj
        }
        return render(request, 'employee.html', context)
    except Exception:
        return HttpResponse('an error occurred')


def others(request):
    try:
        user_obj = UserLogin.objects.get(id=request.session['userId'])
        context = {
            "username": user_obj.username
        }
        return render(request, 'others.html', context)
    except Exception as identifier:
        print(identifier)
        return render(request, 'others.html')


def reports(request):
    try:
        user_obj = UserLogin.objects.get(id=request.session['userId'])
        context = {
            "username": user_obj.username
        }
        return render(request, 'reports.html', context)
    except Exception as identifier:
        print(identifier)
        return render(request, 'reports.html')


def charts(request):
    try:
        user_obj = UserLogin.objects.get(id=request.session['userId'])
        context = {
            "username": user_obj.username
        }
        return render(request, 'charts.html', context)
    except Exception as identifier:
        print(identifier)
        return render(request, 'charts.html')


@csrf_exempt
def fn_create_enquiry(request):
    try:
        if request.method == 'POST':

            lead_source = request.POST['lead_source']
            lead_stage = request.POST['lead_source']

            product = request.POST['product']
            desc = request.POST['lead_source']

            user_obj = UserLogin.objects.get(id=request.session['userId'])
            company_obj = Company(id=request.session['companyId'])
            ass_user_obj = UserLogin.objects.get(
                id=request.POST['assigned'])

            consumer_obj = Consumer.objects.get(id=request.POST['consumer'])
            consumer_name = consumer_obj.fistname + consumer_obj.lastname
            lead_obj = Leads(fk_created_user_id=user_obj,
                             fk_updated_user_id=user_obj,
                             fk_company_id=company_obj,
                             fk_assigned_user_id=ass_user_obj,
                             fk_consumer_id=consumer_obj,
                             lead_title=consumer_name)
            lead_obj.save()

            if lead_obj.id > 0:
                lead_detail_obj = LeadDetails(fk_lead_id=lead_obj,
                                              product=product,
                                              description=desc,
                                              lead_source=lead_source,
                                              lead_stage=lead_stage)
                lead_detail_obj.save()
                return HttpResponse('New enquiry created')
            return HttpResponse('failed')

    except Exception as identifier:
        print(identifier)
        return HttpResponse('an error occurred')


def fn_get_enquiry(request):
    try:
        company_obj = Company(id=request.session['companyId'])
        leads = Leads.objects.filter(fk_company_id=company_obj)
    except Exception as identifier:
        print(identifier)


@csrf_exempt
def fn_create_consumer(request):
    try:
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            gender = request.POST['gender']

            user_obj = UserLogin.objects.get(id=request.session['userId'])
            company_obj = Company.objects.get(id=request.session['companyId'])

            consumer_obj = Consumer(fk_created_user_id=user_obj,
                                    fk_company_id=company_obj,
                                    fistname=fname,
                                    lastname=lname,
                                    email=email,
                                    phone=phone,
                                    address=address,
                                    gender=gender)
            consumer_obj.save()

            if consumer_obj.id > 0:
                return HttpResponse('new consumer created')
            return HttpResponse('failed to create consumer')
    except Exception as e:
        print(e)
        return HttpResponse('an error occurred')


@csrf_exempt
def fn_create_employee(request):
    try:
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            uname = request.POST['uname']
            pword = request.POST['password']
            email = request.POST['email']
            phone = request.POST['phone']
            dob = request.POST['dob']
            location = request.POST['location']
            gender = request.POST['gender']
            role = request.POST['role']

            company_obj = Company.objects.get(id=request.session['companyId'])
            role_obj = UserRole.objects.get(id=role)

            emp_obj = UserLogin(fk_company_id=company_obj,
                                role=role_obj, username=uname, password=pword)

            emp_obj.save()

            if emp_obj.id > 0:
                emp_detail_obj = UserDetails(fk_login_id=emp_obj,
                                             firstname=fname,
                                             mobile=phone,
                                             lastname=lname,
                                             address=location,
                                             dob=dob,
                                             email=email,
                                             gender=gender)
                emp_detail_obj.save()

                if emp_detail_obj.id > 0:
                    return HttpResponse("new employee created")

                return HttpResponse("failed to create employee")
            return HttpResponse("failed to create employee")
    except Exception:
        return HttpResponse('An error occurred')
