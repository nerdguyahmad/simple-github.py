from .errors import *
from .constants import *
from .objects import *
import requests

class Client:
	def __init__(self):
		self._session = requests.Session()

	def fetch_repository(self, repository:str):
		"""Fetches a public repository

		Parameters:
			repository (str) : The full name of repository.

		Returns:
			simplegithub.Repository
		"""
		resp = self._session.get(f'{BASE_URL}/repos/{repository}')
		
		if resp.status_code == 200:
			return Repository(resp.json())

		if resp.status_code == 404:
			raise NotFound(resp.json()['message'])

		if resp.status_code == 403:
			print(resp.json()['message'])

	def fetch_user(self, user:str):
		"""Fetches a user.

		Parameters:
			user (str) : The login (or username) of the user.

		Returns:
			simplegithub.User
		"""
		resp = self._session.get(f'{BASE_URL}/users/{user}')

		if resp.status_code == 200:
			return User(resp.json())

		if resp.status_code == 404:
			raise NotFound(resp.json()['message'])