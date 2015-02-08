from django import forms
from models import Books
from models import Posts
from models import User

class BookForm(forms.ModelForm):

	class Meta:
		model = Books
		fields = ('author','title')	

class PostsForm(forms.ModelForm):

	class Meta:
		model = Posts
		fields = ('author','title','src')

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username','password')	