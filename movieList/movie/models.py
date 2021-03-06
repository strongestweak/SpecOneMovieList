from django.db import models

class Movie(models.Model):

	title = models.CharField(max_length=100, unique=True)
	summary = models.TextField()
	date_screened = models.DateField()
	# director = models.ManyToManyField(Director) can evolve
	director = models.CharField(max_length=100)

	likes = models.PositiveIntegerField(default=0)

	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)