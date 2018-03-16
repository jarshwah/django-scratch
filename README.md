# django-scratch

A project that can be used for testing and interacting with django patches, in
a user focused way.

If you're looking to run the django test suite, then the
[django-box](https://github.com/django/django-box) project is more useful.

The `manage.py` file is configured to load django from a sibling path of the project, to facilitate
testing against the django core repository.

The directory structure should be:

- ~/projects/django/
- ~/projects/django-scratch/

## Initialization

Ensure [pipenv](https://github.com/pypa/pipenv) and [pyenv](https://github.com/pyenv/pyenv) are both installed locally
for best use. Also ensure that the python defined in Pipfile.python_full_version is installed (currently 3.6.4).

```bash
$ git clone https://github.com/django/django
$ git clone https://github.com/jarshwah/django-scratch
$ cd django-scratch
$ pipenv install -d  # if you're using pyenv, this is enough
$ pipenv install -d --python /path/to/python/3.6.4/  # or this if you're not using pyenv
$ cd scratch
$ pipenv run python manage.py migrate
$ pipenv run python manage.py shell_plus
```
