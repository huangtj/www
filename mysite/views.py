# Create your views here.
#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from models import *
from django.db import connection
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/homepage/")
	else:
		return render_to_response('index.html')
	
def login_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		# Correct password, and the user is marked "active"
		auth.login(request, user)
		request.session['username'] = username
		# Redirect to a success page.
		return HttpResponseRedirect("/homepage/")
	else:
     	# Show an error page
		error = True
		message = '用户名或密码错误'
		return render_to_response('index.html',locals())
		

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")

def homepage(request):
	if request.user.is_authenticated():
		homepage=""
		upclassinfo="/upclassinfo/"
		username=request.session['username']
		return render_to_response('homepage.html',locals())
	else:
		return HttpResponseRedirect("/")
	
def reg(request):
	if 'username' in request.GET:
		return render_to_response('reg.html',{'reg_fail':1,'username':request.GET['username']})
	else:
		return render_to_response('reg.html',{'reg_fail':0})

def register(request):
	reg_fail = 1
	username = request.POST['inputUser']
	password = request.POST['pw']
	try:
		m=User.objects.get(username=request.POST['inputUser'])
 		return HttpResponseRedirect('/reg/?username=%s' %username)
	except User.DoesNotExist:
		user = User.objects.create_user(username=username,password=password)
		user.save
		reg_fail = 0
		return HttpResponseRedirect("/reg_op/?id=%s&reg_fail=%d" %(user.id,reg_fail))
		

def reg_op(request):
	reg_fail = request.GET['reg_fail']
	return render_to_response('reg_to_login.html',locals())

def upclassinfo(request):
	homepage="/homepage/"
	upclassinfo=""
	username=request.session['username']
	return render_to_response('upclassinfo.html',locals())

def upload_file(request):
	if request.method == 'POST':
		handle_uploaded_file(request.FILES['file'])
		return HttpResponseRedirect('/upclassinfo/s=1')
	else:
		form = UpFileForm()
		return HttpResponseRedirect('/upclassinfo/s=0')

def handle_uploaded_file(f):
	destination = open("www/upload/file/%s" %f.name, 'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()