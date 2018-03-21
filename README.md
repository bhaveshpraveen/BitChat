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


### Setup
This process can either be done manually or by using Docker.
#### 1. Manually

- Makes sure you have virtualenv installed. If not, run this command
```sh
pip install virtualenv
```

- Create a virtual environment
```sh
virtualenv /path/to/virtualenv
# Replace /path/to/virtualenv with the path in which you want to save your virtual environment
```

- Activate your virtual environment
```sh
source /path/to/virtualenv/bin/activate
# Replace /path/to/virtualenv with your path to virtual environment
```

- Then run,
```sh
pip install -r requirements.txt
```

- You also need to have PostgresSql installed in your machine.

- Make sure you have redis installed or you could use the docker image as specified in the Django Channels Documentation
If you're going to use docker, make sure you have Docker installed and run the following command
```sh
docker run -p 6379:6379 -d redis:2.8
```

Or If you have `redis-server` already installed in your pc. Run this command in your shell
```sh
redis-server
```

- Create a `credentials.txt` file in the root directory of the project. I've set this project to use gmail account. If you intent to use gmail,
add your email in the first line and your password in the following line. Or you could use environment variables, change the code accordingly in the
`settings.py` file.

And then finally run: 
```sh
python3 manage.py runserver
```

#### 2. Using Docker

- Make sure you have Docker installed.

- Create a `credentials.txt` file in the root directory of the project. I've set this project to use gmail. If you intend to use gmail,
add your email in the first line and your password in the next line. Or you could use environment variables, change the code accordingly in the
`settings.py` file.

- Go to `settings.py` file and replace the hosts in the CHANNEL_LAYER with your ip address.
```python
# settings.py
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('# replace this with your ip', 6379)],
        },
    },
}
```
- Then run
```sh
docker-compose up
```