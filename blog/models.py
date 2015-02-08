from django.db import models
from time import time

def get_upload_file_name(instance,file_name):
	return "upload_file/%s_%s" % (str(time()).replace('.','_'),file_name)

class Books(models.Model):
 
  	author = models.CharField(max_length = 30)
  	title = models.CharField(max_length = 100)
  	# bodytext = models.TextField()
  	# timeStamp = models.DateTimeField()
class Posts(models.Model):

	author = models.CharField(max_length = 100)
	title = models.CharField(max_length = 150)
	src = models.ImageField(upload_to = get_upload_file_name)