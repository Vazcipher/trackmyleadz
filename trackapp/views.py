from django.shortcuts import render
from django.http import HttpResponse
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
			context = {
				"username": user_obj.username
			}
			return render(request, 'home.html', context)
		if 'userId' in request.session:
			user_obj = UserLogin.objects.get(id=request.session['userId'])
			context = {
				"username": user_obj.username
			}
			return render(request, 'home.html', context)
		return render(request, 'index.html')
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
		return render(request, 'index.html')
	except Exception as identifier:
		print(identifier)
		return render(request, 'index.html')
