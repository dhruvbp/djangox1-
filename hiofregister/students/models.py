from django.db import models


# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	study = models.CharField(max_length=255)

	def __unicode__(self):
		return '{},{}'.format(self.name, self.email)



