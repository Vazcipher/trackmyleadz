from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,loader
from .models import *


# Create your views here.
def indexPage(request):
	if request.method == 'POST':
		uname = request.POST.get('uname')
		upass = request.POST.get('password')
		if uname == 'admin' and upass == '12345':
			return render(request, 'home.html')
		return render(request, 'index.html', {'msg': 'login failed'})
	return render(request, 'index.html')