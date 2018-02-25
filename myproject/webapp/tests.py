from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


from webapp.models import items
User=get_user_model()

class itemAPITestCase(APITestCase):
	def setUp(self):
		user_obj=User(username='myprojectuser')
		user_obj.set_password("K@lpit4362")
		user_obj.save()
		snippet=items.objects.create(
			user=user_obj,
			name='name',
			price=2
			quantity=2
			pos="A6"
			)

	def test_single_user(self):
		user_count=User.objects.count()
		self.assertEqual(user_count,1)	
