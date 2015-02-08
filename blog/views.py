from django.shortcuts import render_to_response
from forms import PostsForm
from forms import UsersForm
from django.shortcuts import HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from models import Posts
from models import Users
import json
# Create your views here.
def home(request):
	return render_to_response("index.html")
def hello(request):
	name = "Mike"
	return render_to_response('hello.html',{'name':name})

@csrf_exempt
def create(request):
	if request.POST:
		form = PostsForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/list')
	else:
		form = PostsForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('create.html',args)

@csrf_exempt
def register(request):
	if request.POST:
		form = UsersForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/list')
	else:
		form = UsersForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('register.html',args)

def list(request):
	Pics = Posts.objects.all()
	return render_to_response('result.html',{'Pics':Pics})