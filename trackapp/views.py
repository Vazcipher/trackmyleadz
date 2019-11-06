from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import datetime
from .sms_gateway import sendSMS
from .mail_gateway import sendMail
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
                        "username": user_obj.username,
                    }
                    user_details_obj = UserDetails.objects.filter(
                        fk_login_id=user_obj).exists()
                    if user_details_obj:
                        user_obj_ = UserDetails.objects.get(
                            fk_login_id=user_obj)
                        context['user_obj'] = user_obj_
                    else:
                        context['user_obj'] = 0
                    leads = LeadDetails.objects.filter(
                        fk_lead_id__fk_assigned_user_id=user_obj, lead_stage='Open')
                    print(leads)
                    context['leads'] = leads
                    return render(request, 'home.html', context)
                return redirect('/trackapp')
            return redirect('/trackapp')
        return redirect('/trackapp')
    except Exception as identifier:
        print(identifier)
        return render(request, 'index.html', {'msg': 'login failed'})


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
        lead_sources = LeadSource.objects.filter(fk_company_id=company_obj)
        context = {
            "username": user_obj.username,
            "consumer_obj": consumer_obj,
            "emp_obj": emp_obj,
            "pro_obj": product_obj,
            "leads": lead_obj,
            "lead_sources": lead_sources
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
        if request.method == 'POST':
            report_kind = request.POST['report']
            from_date = request.POST['from']
            to_date = request.POST['to']
            company_obj = Company.objects.get(id=request.session['companyId'])
            leads = LeadDetails.objects.filter(
                fk_lead_id__fk_company_id=company_obj, fk_lead_id__created_date__range=(from_date, to_date))
            if report_kind == 'e':
                products = Product.objects.filter(
                    fk_company_id=company_obj).values('product_name')
                report_list = []
                for product_obj in products:
                    product_obj['pro_name'] = product_obj['product_name']
                    product_obj['pro_count'] = 0
                    report_list.append(product_obj)
                for report in report_list:
                    for lead_obj in leads:
                        if report['product_name'] == lead_obj.fk_product_id.product_name:
                            report['pro_count'] = report['pro_count'] + 1
                context['reports'] = report_list
            if report_kind == 's':
                lead_sources = LeadSource.objects.filter(
                    fk_company_id=company_obj).values('source_title')
                report_list = []
                for source_obj in lead_sources:
                    source_obj['pro_name'] = source_obj['source_title']
                    source_obj['pro_count'] = 0
                    report_list.append(source_obj)
                for report in report_list:
                    for lead_obj in leads:
                        if report['source_title'] == lead_obj.fk_lead_source.source_title:
                            report['pro_count'] = report['pro_count'] + 1
            if report_kind == 'ls':
                lead_stages =LeadDetails.objects.filter(fk_company_id= company_obj).values('lead_stage')
                report_list=[]
                for stage_obj in lead_stages :
                    stage_obj['lead'] =stage_obj['lead_stage']
                    stage_obj['lead_count'] = 0
                    report_list.append(stage_obj)
                for report in report_list:
                    for lead_stage_obj in leaddetails:
                        report['lead_count'] = report['lead_count'] + 1
                    
                context['reports'] = report_list
        return render(request, 'reports.html', context)
    except Exception as identifier:
        print(identifier)
        return render(request, 'reports.html')


@csrf_exempt
def fn_create_lead_source(request):
    try:
        if request.method == 'POST':
            user_obj = UserLogin.objects.get(id=request.session['userId'])
            company_obj = Company.objects.get(id=request.session['companyId'])
            source_obj = LeadSource(fk_company_id=company_obj,
                                    fk_created_user_id=user_obj, source_title=request.POST['title'], source_desc=request.POST['desc'])
            source_obj.save()
            if source_obj.id > 0:
                notification_title = '{} created new lead source'.format(
                    user_obj.username)
                notification_obj = Notification(
                    fk_company_id=company_obj, notification_title=notification_title, content_object=source_obj)
                notification_obj.save()
                return JsonResponse({"status": True, "id": source_obj.id, "title": source_obj.source_title})
            return JsonResponse({"status": False})
    except Exception as identifier:
        print(identifier)
        return HttpResponse('An error occured')


@csrf_exempt
def fn_create_enquiry(request):
    try:
        if request.method == 'POST':

            lead_stage = request.POST['lead_stage']

            product = request.POST['product']
            desc = request.POST['description']

            user_obj = UserLogin.objects.get(id=request.session['userId'])
            company_obj = Company(id=request.session['companyId'])
            ass_user_obj = UserLogin.objects.get(
                id=request.POST['assigned'])
            print(ass_user_obj)
            lead_source_obj = LeadSource.objects.get(
                id=request.POST['lead_source'])
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
                                              fk_lead_source=lead_source_obj,
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
                    message = 'Welcome {} to {}'.format(consumer_obj.fistname, company_obj.company_name)
                    sendSMS(consumer_obj.phone, message)
                    sendMail('Hello {}'.format(consumer_obj.fistname), message, [consumer_obj.email])
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
def fn_delete_consumer(request):
    try:
        if request.method == 'POST':
            Consumer.objects.get(id=request.POST['consumer_id']).delete()
            return HttpResponse('Consumer successfully deleted')
    except Exception:
        return HttpResponse('An error occured')


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


@csrf_exempt
def fn_delete_employee(request):
    try:
        if request.method == 'POST':
            user_id = request.POST['user_id']
            user_obj = UserLogin.objects.get(id=user_id)
            UserDetails.objects.get(fk_login_id=user_obj).delete()
            UserLogin.objects.get(id=user_id).delete()
            return HttpResponse('employee deleted')
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
            fk_company_id=company_obj).order_by('-id')[:3].values()
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
        company_obj = Company.objects.get(id=req.session['companyId'])
        product_obj = Product.objects.filter(fk_company_id=company_obj)
        emp_obj = UserLogin.objects.filter(fk_company_id=company_obj)
        if req.method == 'POST':
            product_obj = Product.objects.get(id=req.POST['product'])
            lead_source_obj = LeadSource.objects.get(
                id=req.POST['lead_source'])
            LeadDetails.objects.filter(fk_lead_id__id=req.POST['lead_id']).update(
                fk_product_id=product_obj, description=req.POST['desc'], fk_lead_source=lead_source_obj, lead_stage=req.POST['lead_stage'])
            emp_obj = UserLogin.objects.get(id=req.POST['employee'])
            Leads.objects.filter(id=req.POST['lead_id']).update(
                fk_assigned_user_id=emp_obj, updated_date=datetime.datetime.now().date())
            lead_obj = Leads.objects.get(id=req.POST['lead_id'])
            Consumer.objects.filter(id=lead_obj.fk_consumer_id.id).update(
                email=req.POST['email'], phone=req.POST['phone'])
            return HttpResponse('Enquiry updated')
        lead_obj = LeadDetails.objects.get(fk_lead_id=req.GET['id'])
        lead_sources = LeadSource.objects.filter(fk_company_id=company_obj)
        context = {
            "username": user_obj.username,
            "lead_obj": lead_obj,
            "products": product_obj,
            "employees": emp_obj,
            "lead_sources": lead_sources
        }
        return render(req, 'edit.html', context)
    except Exception as identifier:
        print(identifier)
        return HttpResponse('an error occured')


def fn_view_consumer(req):
    try:
        user_obj = UserLogin.objects.get(id=req.session['userId'])
        consumer_obj = Consumer.objects.get(id=req.GET['id'])
        leads_obj = LeadDetails.objects.filter(
            fk_lead_id__fk_consumer_id=consumer_obj)
        context = {
            "username": user_obj.username,
            "consumer_obj": consumer_obj,
            "leads": leads_obj
        }
        return render(req, 'view_consumer.html', context)
    except Exception as identifier:
        print(identifier)
        return render(req, 'view_consumer.html', {'msg': 'an error occurred'})


def fn_edit_consumer(req):
    try:
        user_obj = UserLogin.objects.get(id=req.session['userId'])
        if req.method == 'POST':
            Consumer.objects.filter(id=req.POST['consumer_id']).update(
                fistname=req.POST['fname'], lastname=req.POST['lname'], email=req.POST['email'],
                phone=req.POST['phone'], address=req.POST['address'], gender=req.POST['gender'])
            return HttpResponse('consumer updated')
        consumer_obj = Consumer.objects.get(id=req.GET['id'])
        context = {
            "username": user_obj.username,
            "consumer_obj": consumer_obj
        }
        return render(req, 'editconsumer.html', context)
    except Exception as identifier:
        print(identifier)
        return HttpResponse('an error occured')


def fn_view_product(req):
    try:
        user_obj = UserLogin.objects.get(id=req.session['userId'])
        pro_obj=Product.objects.get(id=req.GET['id'])
        company_obj=Company.objects.get(id=req.GET['id'])
        product_obj=Product.objects.filter(fk_company_id=pro_obj)
        context = {
            "username": user_obj.username,
            "product_obj": product_obj
        }
        return render(req, 'view_product.html', context)
    except Exception as identifier:
        print(identifier)
        return HttpResponse('an error occured')

def fn_edit_product(req):
    try:
        user_obj = UserLogin.objects.get(id=req.session['userId'])
        if req.method == 'POST':
            Product.objects.filter(id=req.POST['product_id']).update(
                product_code=req.POST['pcode'], product_name=req.POST['pname'], product_cost=req.POST['cost'],
                product_desc=req.POST['desc'])
            return HttpResponse('product updated')
        product_obj = Product.objects.get(id=req.GET['id'])
        context = {
            "username": user_obj.username,
            "product_obj": product_obj
        }
        return render(req, 'editproduct.html', context)
    except Exception as identifier:
        print(identifier)
        return HttpResponse('an error occured')


@csrf_exempt
def fn_save_profile(req):
    try:
        if req.method == 'POST':
            fname = req.POST['fname']
            lname = req.POST['lname']
            email = req.POST['email']
            address = req.POST['address']
            dob = req.POST['dob']
            mobile = req.POST.get('mobile')
            gender = req.POST['gender']
            user_id = req.session['userId']
            user_obj = UserLogin.objects.get(id=user_id)
            userdet_obj = UserDetails(fk_login_id=user_obj, firstname=fname, lastname=lname, address=address,
                                      dob=dob, email=email, mobile=mobile, gender=gender)
            userdet_obj.save()
            if userdet_obj.id > 0:
                return HttpResponse('new profile added')
    except Exception as identifier:
        print(identifier)
        return HttpResponse('error occured')


def fn_edit_employee(req):
    try:
        user_obj = UserLogin.objects.get(id=req.session['userId'])
        if req.method == 'POST':
            print(req.POST['id'])
            UserDetails.objects.filter(id=req.POST['id']).update(
                firstname=req.POST['firstname'], lastname=req.POST['lastname'],
                email=req.POST['email'], mobile=req.POST['mobile'], 
                address=req.POST['location'], gender=req.POST['gender'])
            return HttpResponse('Employee successfully edited')
        emp_obj = UserDetails.objects.get(id=req.GET['id'])
        context = {
            "username": user_obj.username,
            "emp_obj": emp_obj
        }
        return render(req, 'editemployee.html', context)
    except Exception as identifier:
        print(identifier)
        return HttpResponse('an error occured')


def fn_edit_profile(req):
    try:
        user_obj=UserLogin.objects.get(id=req.session['userId'])
        if req.method == 'POST':
            UserDetails.objects.filter(id=req.POST['id']).update( firstname=req.POST['fname'], lastname=req.POST['lname'], address=req.POST['address'],
                                       email=req.POST['email'], mobile=req.POST['mobile'], gender=req.POST['gender'])
            return HttpResponse('profile edited successfully')
        users_obj = UserDetails.objects.get(fk_login_id_id=req.GET['id'])
        context = {
            "users_obj" : users_obj
        }
        return render(req,'editprofile.html',context)
    except Exception as identifier :
        print (identifier)
        return HttpResponse('an error occured')

def fn_view_employee(req):
    try:
        user_obj=UserLogin.objects.get(id=req.session['userId'])
        emp_obj=UserDetails.objects.get(id=req.GET['id'])
        consumer_obj=Consumer.objects.filter()
        context={
            "username":user_obj.username,
            "emp_obj":emp_obj,
        }
        return render(req,'view_employee.html',context)
    except Exception as  identifier:
        print(identifier)
        return render(req,'view_employee.html',{'msg':'error'})
