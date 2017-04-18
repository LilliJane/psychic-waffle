# psychic-waffle

Chatbot for talking statues in The Hague

## ChatterBot with Django

This is a Django app that shows how to create a simple chat bot web
app using Django_ and ChatterBot_.

### Up and running

#### Local

Apply migrations by running `python manage.py migrate`
Start the Django app by running `python manage.py runserver 0.0.0.0:8000`

#### With Docker

A Dockerfile is provided with this repo, as a docker entrypoint which is a script that'll be run each time a container is started.

Before running the container, you need to build the image:

    docker build -t lillijane/django_eps ~/psychic-waffle

When it's built, you can run it with this command:

    docker run -d -p 127.0.0.1:8000:8000 --name eps lillijane/django_eps
It is important to precise the port, especially from the server, because it's the only way to link it with the nginx configuration.

### API documentation

TODO

Further documentation on getting set up with Django and ChatterBot can be
found in the `ChatterBot documentation`.

* [Django](https://www.djangoproject.com)
* [ChatterBot](https://github.com/gunthercox/ChatterBot)
* [ChatterBot documentation](http://chatterbot.readthedocs.io/en/latest/django.html)
