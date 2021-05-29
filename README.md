## :warning: Precaution
This is a highly simple wrapper having very basic functionality. This is meant to be an experimental side project. Don't use it if you are looking for a wrapper that is complex and has a lot of functionality.

# simple-github.py
A highly simple (experimental) wrapper for basic operations with GitHub API.

## Features
This wrapper is very simple but for the sake of making this README large, Here are some features of this wrapper:

- Easy to use and Organized
- Wraps basic endpoints
- Object Oriented design for ease of user
- All objects & methods are [documented](https://github.com/nerdguyahmad/simple-github.py/wiki)

## Quickstart
For more examples and brief docs, Read [Wiki](https://github.com/nerdguyahmad/simple-github.py/wiki)
```py
import simplegithub

client = simplegithub.Client()

repo = client.fetch_repository('nerdguyahmad/simple-github.py') # simplegithub.Repository object.
print(repo.name)
```

## Contributions
Feel free to contribute to this wrapper. Open an issue for breaking changes.
