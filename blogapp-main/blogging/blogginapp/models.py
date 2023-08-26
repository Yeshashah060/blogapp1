from django.db import models

# Create your models here.
class blog(models.Model):
	bname = models.CharField(max_length=50)
	bb = models.CharField(max_length=50)

	def __str__(self):
		 return self.bname;