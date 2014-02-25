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
		setting="/setting/"
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
		return HttpResponseRedirect('/upclassinfo/?s=1')
	else:
		form = UpFileForm()
		return HttpResponseRedirect('/upclassinfo/?s=0')

def handle_uploaded_file(f):
	destination = open("www/upload/file/%s" %f.name, 'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()
	upfile=file(title=f.name,address="www/upload/file/%s" %f.name)
	upfile.save()

from django.core.servers.basehttp import FileWrapper
import mimetypes
import os

def file_download(request):
	file_list = []
	i=1
	for file_item in file.objects.all(): 
		file_dict = {} 
		file_dict['num']=i
		i=i+1
		file_dict['title'] = file_item.title
		file_dict['address'] = file_item.address 
		file_list.append(file_dict) 
	username=request.session['username']
	return render_to_response('file_download.html',{ 'file_list': file_list , 'homepage':homepage, 'upclassinfo':upclassinfo,'username':username})

def file_download_op(request,filename):  
	wrapper = FileWrapper(open("www/upload/file/%s" %filename, 'rb'))
	content_type = mimetypes.guess_type("www/upload/file/%s" %filename)[0]
	response = HttpResponse(wrapper, mimetype='content_type')
	response['Content-Disposition'] = "attachment; filename=%s" % filename.encode('utf-8')
	return response

def setting(request):
	username=request.session['username']
	return render_to_response('setting.html',locals())
	
def setting_op(request):
	try:
		p = User.objects.get(username=request.POST['username'])
	except User.DoesNotExist:
		error=True
		message="操作出错！无此用户"
	else:
		if request.POST['newpw']!=request.POST['newpw2']:
			error=True
			message="两次输入的密码不一致"
		else:
			p.set_password(request.POST['newpw'])
			p.save()
			success=True
			message="修改成功"
	username=request.session['username']
	return render_to_response('setting.html',locals())

def upsoftware(request):
 	username=request.session['username']
	return render_to_response('upsoftware.html',locals())
 
def upsoftware_op(request):
	if request.method == 'POST':
		handle_uploaded_sf(request.FILES['file'])
		return HttpResponseRedirect('/upsoftware/s=1')
	else:
		form = UpFileForm()
		return HttpResponseRedirect('/upsoftware/s=0')

def handle_uploaded_sf(f):
	destination = open("www/upload/software/%s" %f.name, 'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()
	upfile=software(title=f.name,address="www/upload/software/%s" %f.name)
	upfile.save()

def software_download(request):
	file_list = []
	i=1
	for file_item in software.objects.all(): 
		file_dict = {} 
		file_dict['num']=i
		i=i+1
		file_dict['title'] = file_item.title
		file_dict['address'] = file_item.address 
		file_list.append(file_dict)
 	username=request.session['username']
	return render_to_response('software_download.html',locals())

def software_download_op(request,filename):
	wrapper = FileWrapper(open("www/upload/software/%s" %filename, 'rb'))
	content_type = mimetypes.guess_type("www/upload/software/%s" %filename)[0]
	response = HttpResponse(wrapper, mimetype='content_type')
	response['Content-Disposition'] = "attachment; filename=%s" % filename.encode('utf-8')
	return response

def other_download(request):
	file_list = []
	i=1
	for file_item in other_file.objects.all(): 
		file_dict = {} 
		file_dict['num']=i
		i=i+1
		file_dict['title'] = file_item.title
		file_dict['address'] = file_item.address 
		file_list.append(file_dict)
 	username=request.session['username']
	return render_to_response('software_download.html',locals())

def other_download_op(request):
	wrapper = FileWrapper(open("www/upload/other/%s" %filename, 'rb'))
	content_type = mimetypes.guess_type("www/upload/other/%s" %filename)[0]
	response = HttpResponse(wrapper, mimetype='content_type')
	response['Content-Disposition'] = "attachment; filename=%s" % filename.encode('utf-8')
	return response

def upother(request):
	username=request.session['username']
	return render_to_response('upother.html',locals())

def upother_op(request):
	if request.method == 'POST':
		handle_uploaded_other(request.FILES['file'])
		return HttpResponseRedirect('/upother/s=1')
	else:
		form = UpFileForm()
		return HttpResponseRedirect('/upother/s=0')

def handle_uploaded_other(f):
	destination = open("www/upload/other/%s" %f.name, 'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()
	upfile=other_file(title=f.name,address="www/upload/other/%s" %f.name)
	upfile.save()

def notice(request):
	return HttpResponse("开发中<a href='javascript:history.back(-1)'>返回上一页</a>")