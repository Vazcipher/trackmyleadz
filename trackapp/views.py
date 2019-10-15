from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
        product_obj = Product.objects.filter(fk_company_id=company_obj)
        lead_obj = LeadDetails.objects.filter(
            fk_lead_id__fk_company_id=company_obj)
        context = {
            "username": user_obj.username,
            "consumer_obj": consumer_obj,
            "emp_obj": emp_obj,
            "pro_obj": product_obj,
            "leads": lead_obj
        }
        return render(request, 'enquires.html', context)
    except Exception:
        return HttpResponse('an error occurred')


def consumer(request):
    try:
        user_obj = UserLogin.objects.get(id=request.session['userId'])
        company_obj = Company.objects.get(id=request.session['companyId'])

        cons_obj = Consumer.objects.filter(fk_company_id=company_obj)
        context = {
            "username": user_obj.username,
            "consmr_obj": cons_obj
        }
        return render(request, 'consumer.html', context)
    except Exception:
        return HttpResponse('an error occurred')


def employee(request):
    try:
        user_obj = UserLogin.objects.get(id=request.session['userId'])
        company_obj = Company.objects.get(id=request.session['companyId'])
        role_obj = UserRole.objects.filter(fk_company_id=company_obj)
        userdet_obj = UserDetails.objects.filter(
            fk_login_id__fk_company_id=company_obj)
        context = {
            "username": user_obj.username,
            "roles": role_obj,
            "userdetail": userdet_obj
        }
        return render(request, 'employee.html', context)
    except Exception:
        return HttpResponse('an error occurred')


def product(request):
    try:
        user_obj = UserLogin.objects.get(id=request.session['userId'])
        company_obj = Company.objects.get(id=request.session['companyId'])

        product_obj = Product.objects.filter(fk_company_id=company_obj)

        context = {
            "username": user_obj.username,
            "pro_obj": product_obj
        }
        return render(request, 'product.html', context)
    except Exception as identifier:
        print(identifier)
        return render(request, 'product.html')


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
            lead_stage = request.POST['lead_stage']

            product = request.POST['product']
            desc = request.POST['description']

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
                product_obj = Product.objects.get(id=product)
                lead_detail_obj = LeadDetails(fk_lead_id=lead_obj,
                                              fk_product_id=product_obj,
                                              description=desc,
                                              lead_source=lead_source,
                                              lead_stage=lead_stage)
                lead_detail_obj.save()
                if lead_detail_obj.id > 0:
                    notification_title = '{} created new enquire on {}'.format(
                        user_obj.username, consumer_obj.fistname)
                    notification_obj = Notification(
                        fk_company_id=company_obj, notification_title=notification_title, content_object=lead_detail_obj)
                    notification_obj.save()
                    return HttpResponse('New enquiry created')
            return HttpResponse('failed')

    except Exception as identifier:
        print(identifier)
        return HttpResponse('an error occurred')


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

            check_consumer = Consumer.objects.filter(email=email).exists()
            if not check_consumer:
                user_obj = UserLogin.objects.get(id=request.session['userId'])
                company_obj = Company.objects.get(
                    id=request.session['companyId'])

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
                    notification_title = "{} created new consumer {}".format(
                        user_obj.username, consumer_obj.fistname)
                    notification_obj = Notification(
                        fk_company_id=company_obj, notification_title=notification_title, content_object=consumer_obj)
                    notification_obj.save()
                    return HttpResponse('new consumer created')
                return HttpResponse('failed to create consumer')
            return HttpResponse('consumer already exist')
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
            check_emp_exist = UserLogin.objects.filter(username=uname).exists()
            if not check_emp_exist:
                company_obj = Company.objects.get(
                    id=request.session['companyId'])
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
                        current_user_obj = UserLogin.objects.get(
                            id=request.session['userId'])
                        notification_title = '{} added new employee {}'.format(
                            current_user_obj.username, emp_obj.username)
                        print(notification_title)
                        notification_obj = Notification(
                            fk_company_id=company_obj, notification_title=notification_title, content_object=emp_detail_obj)
                        notification_obj.save()
                        return HttpResponse("new employee created")

                    return HttpResponse("failed to create employee")
                return HttpResponse("failed to create employee")
            return HttpResponse('Username already exisit')
    except Exception:
        return HttpResponse('An error occurred')


@csrf_exempt
def fn_create_product(request):
    try:
        if request.method == 'POST':
            code = request.POST['pro_code']
            name = request.POST['pro_name']
            cost = request.POST['pro_cost']
            desc = request.POST['pro_desc']

            created_user_obj = UserLogin.objects.get(
                id=request.session['userId'])
            company_obj = Company.objects.get(id=request.session['companyId'])
            pro_code_exists = Product.objects.filter(
                product_code=code).exists()
            if not pro_code_exists:
                product_obj = Product(fk_created_user_id=created_user_obj, fk_company_id=company_obj,
                                      product_code=code, product_name=name, product_cost=cost, product_desc=desc)
                product_obj.save()
                if product_obj.id > 0:
                    return HttpResponse('new product created')
                return HttpResponse('failed to create product')
            return HttpResponse('product exists')
    except Exception:
        return HttpResponse('An error occurred')


@csrf_exempt
def fn_delete_product(request):
    try:
        if request.method == 'POST':
            Product.objects.get(id=request.POST['pro_id']).delete()
            return HttpResponse('Product successfully deleted')
    except Exception:
        return HttpResponse('an error occurred')


@csrf_exempt
def fn_delete_enquiry(request):
    try:
        if request.method == 'POST':
            lead_id = request.POST['lead_id']
            lead_obj = Leads.objects.get(id=lead_id)
            LeadDetails.objects.get(fk_lead_id=lead_obj).delete()
            Leads.objects.get(id=lead_id).delete()
            return HttpResponse('enquiry deleted')
    except Exception:
        return HttpResponse('an error occurred')


def fn_follow_up(request):
    try:
        user_obj = UserLogin.objects.get(id=request.session['userId'])
        lead_detail_obj = LeadDetails.objects.get(
            fk_lead_id__id=request.GET['id'])
        follow_ups = FollowUp.objects.filter(
            fk_lead_id=lead_detail_obj.fk_lead_id)
        context = {
            "username": user_obj.username,
            "lead_obj": lead_detail_obj,
            "followups": follow_ups
        }
        return render(request, 'followup.html', context)
    except Exception as identifier:
        print(identifier)
        return HttpResponse('an error occurred')


@csrf_exempt
def fn_save_follow_up(req):
    try:
        if req.method == 'POST':
            lead_id = req.POST['lead_id']
            followup_title = req.POST['title']
            followup_desc = req.POST['desc']

            lead_obj = Leads.objects.get(id=lead_id)
            user_obj = UserLogin.objects.get(id=req.session['userId'])
            company_obj = Company.objects.get(id=req.session['companyId'])

            followup_obj = FollowUp(fk_lead_id=lead_obj, fk_created_user_id=user_obj,
                                    fk_company_id=company_obj, followup_title=followup_title,
                                    followup_description=followup_desc)
            followup_obj.save()
            if followup_obj.id > 0:
                return HttpResponse('New followup added')
    except Exception as identifier:
        print(identifier)
        return HttpResponse('An error occurred')


@csrf_exempt
def fn_delete_followup(req):
    try:
        if req.method == 'POST':
            FollowUp.objects.get(id=req.POST['followup_id']).delete()
            return HttpResponse('followup removed')
    except Exception as identifier:
        print(identifier)
        return HttpResponse('an error occured')


@csrf_exempt
def fn_finish_followup(req):
    try:
        if req.method == 'POST':
            FollowUp.objects.filter(id=req.POST['followup_id']).update(
                completed_status=True)
            return HttpResponse('Followup completed')
    except expression as identifier:
        print(identifier)
        return HttpResponse('an error occurred')


@csrf_exempt
def fn_get_notifications(request):
    try:
        company_obj = Company.objects.get(id=request.session['companyId'])
        notifications = Notification.objects.filter(
            fk_company_id=company_obj).values()
        return JsonResponse({"notifications": list(notifications)})
    except Exception as identifier:
        print(identifier)
        return JsonResponse({"res": "error"})


@csrf_exempt
def fn_change_password(req):
    try:
        if req.method == 'POST':
            user_obj = UserLogin.objects.get(id=req.session['userId'])
            if user_obj.password == req.POST['oldpass']:
                UserLogin.objects.filter(id=req.session['userId']).update(
                    password=req.POST['newpass'])
                return HttpResponse('Successfully changed password')
            return HttpResponse('old password does not match')
    except Exception as identifier:
        print(identifier)
        return HttpResponse('an error occured')


def fn_edit_enquiry(req):
    try:
        user_obj = UserLogin.objects.get(id=req.session['userId'])
        context = {
            "username": user_obj.username,
        }
        return render(req, 'edit.html', context)
    except Exception as identifier:
        print(identifier)
        return HttpResponse('an error occured')
