from .constants import BASE_URL
import requests

class Repository:
	'''Represents a github *proper* repository. This has more functionality then partial one.'''
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
	"""Represents a *proper* user. This has a lot more then simplegithub.PartialUser class."""
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
		return [PartialGist(gist) for gist in gists]

	def fetch_subscriptions(self):
		"""Fetches the repositories user has subscribed to.
		
		Returns:
			list[simplegithub.PartialRepository]
		"""
		subs = self._session.get(f'{BASE_URL}/users/{self.login}/subscriptions').json()
		return [PartialRepository(sub) for sub in subs]

class ChangeStatus:
	'''Represents the changes of a history item'''
	def __init__(self, data):
		for key in data:
			setattr(self, key, data[key])

class HistoryItem:
	'''Represents a history item of a Gist revision history'''
	def __init__(self, data):
		for key in data:
			if key == 'user':
				setattr(self, key, PartialUser(data[key]))
			elif key == 'owner':
				setattr(self, key, PartialUser(data[key]))
			elif key == 'change_status':
				setattr(self, key, ChangeStatus(data[key]))
			else:
				setattr(self, key, data[key])

class PartialGist:
	'''Represents a partial gist. (This doesn't has history and some other attributes)'''
	def __init__(self, data):
		for key in data:
			if key == 'files':
				self.files = []
				for file in data[key].keys():
					self.files.append(File(name=file, data=data[key][file]))
			elif key == 'owner':
				setattr(self, key, PartialUser(data[key]))

			else:
				setattr(self, key, data[key])

		self._session = requests.Session()

	def fetch_gist(self):
		'''Returns the Gist object of this partial Gist'''
		resp = self._session.get(self.url)
		return Gist(resp.json())


class Gist:
	'''Represents a github gist.'''
	def __init__(self, data):
		for key in data:
			if key == 'files':
				self.files = []
				for file in data[key].keys():
					self.files.append(File(name=file, data=data[key][file]))
			elif key == 'owner':
				setattr(self, key, PartialUser(data[key]))
			elif key == 'history':
				setattr(self, key, [HistoryItem(x) for x in data[key]])
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
		resp = self._session.get(self.forks_url).json()
		# No class for commit yet exists so this returns the list raw dict objects.
		return [x for x in resp]



class File:
	'''Represents a github file (generally returned from gists).'''
	def __init__(self, name, data):
		self.name = name
		for key in data.keys():
			setattr(self, key, data[key])

		self._session = requests.Session()

	def fetch_raw(self):
		"""This fetches the raw content of the file. (Basically gets the file src)"""
		resp = self._session.get(self.raw_url)
		return resp.text




class License:
	"""Represents a *proper* license. This has a lot more then simplegithub.PartialLicense class."""
	def __init__(self, data):
		for key in data:
			setattr(self, key, data[key])

class Item:
	'''Represents an item from the repository content'''
	def __init__(self, data):
		for key in data:
			setattr(self, key, data[key])

		self._session = requests.Session()

	def fetch_dir(self):
		"""Fetches the items of a directory

		Returns:
			list[Item]
		"""
		if not self.type == 'dir':
			raise TypeError("The item is not a directory.")
			return

		resp = self._session.get(self._links['self']).json()
		return [Item(item) for item in resp]

class PartialRepository:
	'''Represents a github *partial* repository'''
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
	'''Represents a *partial* user. A partial user doesn't has everything a User has.'''
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
	"""Represents a *partial* license. A partial license doesn't has entire detail of license."""
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