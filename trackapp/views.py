from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template,loader
from .models import *


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
					user_obj = UserLogin.objects.get(id=request.session['userId'])
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
		context = {
			"username": user_obj.username
		}
		return render(request, 'enquires.html', context)
	except Exception as identifier:
		print(identifier)

def consumer(request):
	try:
		user_obj = UserLogin.objects.get(id=request.session['userId'])
		context = {
			"username": user_obj.username
		}
		return render(request, 'consumer.html', context)
	except Exception as identifier:
		print(identifier)

def employee(request):
	try:
		user_obj = UserLogin.objects.get(id=request.session['userId'])
		context = {
			"username": user_obj.username
		}
		return render(request, 'employee.html', context)
	except Exception as identifier:
		print(identifier)

def others(request):
	try:
		user_obj = UserLogin.objects.get(id=request.session['userId'])
		context = {
			"username": user_obj.username
		}
		return render(request, 'others.html', context)
	except Exception as identifier:
		print(identifier)


def reports(request):
	try:
		user_obj = UserLogin.objects.get(id=request.session['userId'])
		context = {
			"username": user_obj.username
		}
		return render(request, 'reports.html', context)
	except Exception as identifier:
		print(identifier)

def charts(request):
	try:
		user_obj = UserLogin.objects.get(id=request.session['userId'])
		context = {
			"username": user_obj.username
		}
		return render(request, 'charts.html', context)
	except Exception as identifier:
		print(identifier)