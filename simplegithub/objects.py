from .constants import BASE_URL
import requests

class Repository:
	'''Represents a github *proper* repository. This has more functionality then partial one.
	
	Attributes
	----------
	See all attributes at https://nerdguyahmad.gitbook.io/simplegithub/objects/repository#attributes

	Methods
	-------
	See all methods at https://nerdguyahmad.gitbook.io/simplegithub/objects/repository#methods
	'''
	def __init__(self, data):
		_objects = {
			"license": PartialLicense,
			"owner": PartialUser
		}

		for key in data.keys():
			if key in _objects:
				setattr(self, key, _objects[key](data[key]))
			else:
				setattr(self, key, data[key])

		self._session = requests.Session()

	def fetch_forks(self):
		"""Fetches the forks of the repository
		
		Returns:
			list[simplecord.Repository]
		"""
		resp = self._session.get(self.forks_url)
		return [Repository(x) for x in resp.json()]

	def fetch_contents(self):
		"""Fetches the content of the repository
		
		Returns:
			list[simplecord.Item]
		"""
		resp = self._session.get(self.contents_url.replace('/{+path}', ''))
		return [Item(x) for x in resp.json()]


class User:
	"""Represents a *proper* user. This has a lot more then simplegithub.PartialUser class.
	
	Attributes
	----------
	See all attributes at https://nerdguyahmad.gitbook.io/simplegithub/objects/user#attributes

	Methods
	-------
	See all attributes at https://nerdguyahmad.gitbook.io/simplegithub/objects/user#methods
	"""
	def __init__(self, data):
		for key in data:
			setattr(self, key, data[key])

		self._session = requests.Session()

	def fetch_repos(self):
		"""Fetches the public repositories of user
		
		Returns:
			list[simplegithub.Repository]
		"""
		repos = self._session.get(f'{BASE_URL}/users/{self.login}/repos').json()
		return [PartialRepository(repo) for repo in repos]

	def fetch_followers(self):
		"""Fetches the followers of user
		
		Returns:
			list[simplegithub.PartialUser]
		"""
		followers = self._session.get(f'{BASE_URL}/users/{self.login}/followers').json()
		return [PartialUser(follower) for follower in followers]

	def fetch_following(self):
		"""Fetches the users that user follows.
		
		Returns:
			list[simplegithub.PartialUser]
		"""
		following = self._session.get(f'{BASE_URL}/users/{self.login}/following').json()
		return [PartialUser(user) for user in following]

	def fetch_starred(self):
		"""Fetches the repositories that user has starred.
		
		Returns:
			list[simplegithub.PartialRepository]
		"""
		following = self._session.get(f'{BASE_URL}/users/{self.login}/starred').json()
		return [PartialRepository(user) for user in following]

	def fetch_gists(self):
		"""Fetches the gists that user has.
		
		Returns:
			list[simplegithub.Gist]
		"""
		gists = self._session.get(f'{BASE_URL}/users/{self.login}/gists').json()
		return [Gist(gist) for gist in gists]

class Gist:
	'''Represents a github gist.

	Attributes
	----------
	See all attributes at https://nerdguyahmad.gitbook.io/simplegithub/objects/license#attributes


	'''
	def __init__(self, data):
		for key in data:
			if key == 'files':
				self.files = []
				for file in self.files:
					self.files.append(File(file))
			else:
				setattr(self, key, data[key])

	def fetch_forks(self):
		"""Fetches the forks of the gist
		
		Returns:
			list[simplecord.Gist]
		"""
		resp = self._session.get(self.forks_url)
		return [Gist(x) for x in resp.json()]

	def fetch_commits(self):
		"""Fetches the forks of the gist
		
		Returns:
			list[simplecord.Gist]
		"""
		resp = self._session.get(self.forks_url)
		return [Commit(x) for x in resp.json()]

class File:
	'''Represents a github file.

	Attributes
	----------
	See all attributes at https://nerdguyahmad.gitbook.io/simplegithub/objects/file#attributes


	'''
	def __init__(self, data):
		...
		

class License:
	"""Represents a *proper* license. This has a lot more then simplegithub.PartialLicense class.
	
	Attributes
	----------

	See all attributes at https://nerdguyahmad.gitbook.io/simplegithub/objects/license#attributes
	"""
	def __init__(self, data):
		for key in data:
			setattr(self, key, data[key])

class Item:
	'''Represents an item from the repository content'''
	def __init__(self, data):
		for key in data:
			setattr(self, key, data[key])

		self._session = requests.Session()

	def fetch_dir(self, dir):
		"""Fetches the items of a directory

		Returns:
			list[Item]
		"""
		if not dir.type == 'dir':
			raise TypeError("The item is not a directory.")
			return

		resp = self.session.get(dir._links['self']).json()
		return [Item(item) for item in resp]

class PartialRepository:
	'''Represents a github *partial* repository
	
	Attributes
	----------
	See all attributes at https://nerdguyahmad.gitbook.io/simplegithub/objects/partial-repository#attributes

	Methods
	-------
	See all methods at https://nerdguyahmad.gitbook.io/simplegithub/objects/partial-repository#methods
	'''
	def __init__(self, data):
		for key in data:
			setattr(self, key, data[key])

	
	def fetch_repository(self):
		"""Returns the Repository object of this partial repository
	
		Returns:
			simplegithub.Repository
		"""
		resp = requests.get(f'{BASE_URL}/repos/{self.full_name}')

		return Repository(resp.json())

class PartialUser:
	'''Represents a *partial* user. A partial user doesn't has everything a User has.

	Attributes
	----------
	See all attributes at https://nerdguyahmad.gitbook.io/simplegithub/objects/partial-user#attributes
	
	Methods
	-------
	See all methods at https://nerdguyahmad.gitbook.io/simplegithub/objects/partial-user#methods
	'''
	def __init__(self, data):
		for key in data:
			setattr(self, key, data[key])

		self._session = requests.Session()

	def fetch_user(self):
		"""Returns the User object of this partial user.
	
		Returns:
			simplegithub.User
		"""
		resp = requests.get(f'{BASE_URL}/users/{self.login}')

		return User(resp.json())


class PartialLicense:
	"""Represents a *partial* license. A partial license doesn't has entire detail of license.

	Attributes
	----------
	See all attributes at https://nerdguyahmad.gitbook.io/simplegithub/objects/partial-license#attributes

	Methods
	-------
	See all methods at https://nerdguyahmad.gitbook.io/simplegithub/objects/partial-repository#methods
	"""
	def __init__(self, data):
		for key in data:
			setattr(self, key, data[key])

	
	def fetch_license(self):
		"""Returns the License object of this partial license
	
		Returns:
			simplegithub.License
		"""
		resp = requests.get(f'{BASE_URL}/licenses/{self.key}')

		return License(resp.json())