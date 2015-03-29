from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
from forms import PostsForm
from forms import UsersForm
from django.shortcuts import HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from models import Posts
from models import Comments
from models import Users
import json
# Create your views here.
def home(request):
	if 'username' in request.session:
		username = request.session["username"]
	else:
		username =""
	return render_to_response("index.html",{'username':username})
def hello(request):
	name = "Mike"
	return render_to_response('hello.html',{'name':name})

@csrf_exempt
def create(request):
	if 'username' in request.session:
		username = request.session["username"]
	else:
		username =""
	if request.POST:
		form = PostsForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/list',{'username':username})
	else:
		form = PostsForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('create.html',args)

@csrf_exempt
def register(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		form = UsersForm(request.POST)
		if form.is_valid():
			form.save()
			request.session["username"]= username
			request.session["password"]= password
			return HttpResponseRedirect('/list')
	else:
		form = UsersForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('register.html',args)

@csrf_exempt
def login(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = Users.objects.get(username=username)
		form = UsersForm(request.POST,request.FILES)
		if user.password == password:
			request.session["username"] = username
			request.session["password"] = password
			return HttpResponseRedirect('/list')
	else:
		form = UsersForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('login.html',args)

def list(request):
	Pics = Posts.objects.all()
	if 'username' in request.session:
		username = request.session["username"]
	else:
		username =""
	# print Pics[0].src
	return render_to_response('result.html',{'Pics':Pics,'username':username})
	# return HttpResponse(serializers.serialize("json", Pics))

def detail(request,id):
	result = Posts.objects.get(id=int(id))
	comments =Comments.objects.filter(linkid=int(id))
	# return HttpResponse(str(result))
	return render_to_response('detail.html',{'result':result,'comment':comments})

def logout(request):
    del request.session["username"]
    return HttpResponseRedirect("/")

@csrf_exempt
def comment(request):
	error = ""
	if 'username' in request.session:
		username = request.session["username"]
	else:
		username =""
		error = "you need to log in to comment"
	if request.GET and username!="":
		content = request.GET['content']
		linkid = request.GET['id']
		p = Comments(author= username,content= content,linkid= linkid)
		p.save()
		return JsonResponse({'contnet':content,'result':True,'error':error})
	else:		
	    return JsonResponse({'result':False,'error':error})

		







