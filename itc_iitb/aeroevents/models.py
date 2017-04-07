from django.db import models

class Event(models.Model):
	title = models.CharField(max_length=140)
	happeningdate = models.DateTimeField()
	smalldescription = 	models.TextField()
	largedescription = models.TextField()
	imagelink = models.CharField(max_length=500)
	drivelink = models.CharField(max_length=500)
	date = models.DateTimeField()
	def __str__(self):
		return self.title
