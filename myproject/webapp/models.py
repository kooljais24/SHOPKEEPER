from django.db import models

# Create your models here.
class items(models.Model):
	name=models.CharField(max_length=20)
	price=models.IntegerField()
	quantity=models.IntegerField()
	pos=models.CharField(max_length=3)

	def __str__(self):
		return self.name