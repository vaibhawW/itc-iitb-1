from django.db import models

class Events(models.Model):
	title = models.CharField(max_length=140)
	happeningdate = models.DateTimeField()
	smalldiscription = 	models.TextField()
	largediscription = models.TextField()
	imagelink = models.CharField(max_length=500)
	drivelink = models.CharField(max_length=500)
	date = models.DateTimeField()
	def __str__(self):
		return self.title
