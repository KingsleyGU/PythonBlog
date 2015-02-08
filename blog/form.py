from django import forms
from models import Books
from models import Posts
from models import Users

class BookForm(forms.ModelForm):

	class Meta:
		model = Books
		fields = ('author','title')	

class PostsForm(forms.ModelForm):

	class Meta:
		model = Posts
		fields = ('author','title','src')

class UsersForm(forms.ModelForm):

	class Meta:
		model = Users
		fields = ('username','password')	