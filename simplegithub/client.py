from .errors import *
from .constants import *
from .objects import *
import requests

class Client:
	'''This is the main class to interact with API'''
	def __init__(self):
		self._session = requests.Session()

	def fetch_repository(self, repository:str):
		"""Fetches a public repository

		Parameters:
			repository (str) : The full name of repository.

		Returns:
			simplegithub.Repository

		Raises:
			simplegithub.NotFound
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

		Raises:
			simplegithub.NotFound
		"""
		resp = self._session.get(f'{BASE_URL}/users/{user}')

		if resp.status_code == 200:
			return User(resp.json())

		if resp.status_code == 404:
			raise NotFound(resp.json()['message'])

		if resp.status_code == 403:
			print(resp.json()['message'])

	def fetch_gist(self, id:str=None):
		"""Fetches a gist.

		Parameters:
			id (str) : The ID of the gist.

		Returns:
			simplegithub.Gist

		Raises:
			simplegithub.NotFound
		"""
		resp = self._session.get(f'{BASE_URL}/gists/{id}')

		if resp.status_code == 200:
			return Gist(resp.json())

		if resp.status_code == 404:
			raise NotFound(resp.json()['message'])

		if resp.status_code == 403:
			print(resp.json()['message'])

	def fetch_license(self, key:str=None):
		"""Fetches a license.

		Parameters:
			key (str) : The license key. e.g `mit`

		Returns:
			simplegithub.License

		Raises:
			simplegithub.NotFound
		"""
		resp = self._session.get(f'{BASE_URL}/licenses/{key}')

		if resp.status_code == 200:
			return License(resp.json())

		if resp.status_code == 404:
			raise NotFound(resp.json()['message'])

		if resp.status_code == 403:
			print(resp.json()['message'])