from django import forms
from models import Books
from models import Posts

class BookForm(forms.ModelForm):

	class Meta:
		model = Books
		fields = ('author','title')	

class PostsForm(forms.ModelForm):

	class Meta:
		model = Posts
		fields = ('author','title','src')