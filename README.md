# BitChat

A simple chat application that uses [Django Channels v2](https://channels.readthedocs.io/en/latest/) for real time updates.

This is an extension/fork of the [Django Channels tutorial](https://channels.readthedocs.io/en/latest/tutorial/)

### What's new ?
- Messages are now stored in Database
- Added User Registration

The messages are now persistent and they can accessed across different sessions.
User Registration through [Registration package](https://django-registration.readthedocs.io/en/2.4.1/).
Templates for the registration obtained from [macdhuibh/django-registration-templates
](https://github.com/macdhuibh/django-registration-templates).

### Getting Setup
```sh
pip install -r requirements.txt
```

Make sure you have redis installed or you could use the docker image as specified in the Django Channels Documentation
If you're going to use docker, make sure you have Docker installed and run the following command
```sh
docker run -p 6379:6379 -d redis:2.8
```
If you have `redis-server` already installed in your pc. Run this command in your shell
```sh
redis-server
```

Create a `credentials.txt` file in the root directory of the project. I've set this project to use gmail account. If you intent to use gmail,
add your email in the first line and your password in the following line. Or you could use environment variables, change the code accordingly in the
`settings.py` file.

```sh
python3 manage.py runserver
```


