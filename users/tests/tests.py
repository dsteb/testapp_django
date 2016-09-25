from django.test import TestCase, Client

from users.models import UserProfile
from tweety.models import Tweet

class UsersTests(TestCase):

	def test_registration(self):
		c = Client()
		response = c.post('/users/register/', {'username': 'test@gmail.com', 'password1': 'test', 'password2': 'test'}, follow=True)
		# successful registration -> redirect to home
		self.assertEquals(('/', 302), response.redirect_chain[0])
		

		response = c.get('/users/register/', follow=True)
		# get should redirect to home if the user is logged in
		self.assertEquals(('/', 302), response.redirect_chain[0])

		c.logout()

	def test_login(self):
		c = Client()

		data = {'username': 'test1@gmail.com', 'password1': 'test', 'password2': 'test'}
		response = c.post('/users/register/', data, follow=True)
		c.logout()

		# successful login -> redirect to home
		data = {'username': 'test1@gmail.com', 'password': 'test'}
		response = c.post('/users/login/', data, follow=True)
		self.assertEquals(('/', 302), response.redirect_chain[0])

		# get should redirect to home if the user is logged in
		response = c.get('/users/login/', follow=True)
		self.assertEquals(('/', 302), response.redirect_chain[0])

		c.logout()

	def test_logout(self):
		c = Client()

		data = {'username': 'test2@gmail.com', 'password1': 'test', 'password2': 'test'}
		response = c.post('/users/register/', data, follow=True)
		c.logout()

		response = c.get('/')
		latest_tweets = response.context[0]['latest_tweets']

