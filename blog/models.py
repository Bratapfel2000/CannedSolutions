from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	image = models.ImageField(default='default2.jpg', upload_to='post_pics')
	image2 = models.ImageField(default='default2.jpg', upload_to='post_pics2')

	#if user is deleted, post will also be deleted
	author = models.ForeignKey(User, on_delete = models.CASCADE) 

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})
