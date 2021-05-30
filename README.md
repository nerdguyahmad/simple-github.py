### :warning: Precaution

This is a highly simple wrapper having very basic functionality. This is meant to be an experimental side project just for fun. Do not use it because it doesn't has a documentation (you have to be brave enough to read the source code). This wrapper is not a complex one so please use a wrapper that is documented and has more functionality.

# simple-github.py

A highly simple \(experimental\) wrapper for basic operations with GitHub API.

## Features

This wrapper is very simple but for the sake of making this README large, Here are some features of this wrapper:

* Easy to use and Organized
* Wraps basic endpoints
* Object Oriented design for ease of user
* All attributes are same as provided by Github API.

## Quickstart

For more examples and brief docs, Read [Wiki](https://github.com/nerdguyahmad/simple-github.py/wiki)

### Fetching repository
```python
import simplegithub

client = simplegithub.Client()

repo = client.fetch_repository('nerdguyahmad/simple-github.py') # simplegithub.Repository object.
print(repo.fullname, repo.owner.login) # There are more attributes.
```

### Fetching User (and optionally, repository of users)
```python
import simplegithub

client = simplegithub.Client()

user = client.fetch_user('nerdguyahmad') # simplegithub.User object.
print(user.login)

user_repos = user.fetch_repos() # List of simplegitub.PartialRepository objects.

for i in user_repos:
  print(i.fullname)
```

***There are many more objects, methods and attributes that are not documented. If you want to see them, read the source code.***

## Contributions

Feel free to contribute to this wrapper. Open an issue for breaking changes. The only thing other then more methods this wrapper needs is a documentation. If you are brave enough to read the source code and document it then resource you need is [here](for-contributor/make-the-doc.MD).
