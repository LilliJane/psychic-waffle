# psychic-waffle

Chatbot for talking statues in The Hague

## ChatterBot with Django

This is a Django app that shows how to create a simple chat bot web
app using Django_ and ChatterBot_.

### Up and running

#### Local

Apply migrations by running 
    `python manage.py migrate`

Train the bot by running `python manage.py train`

If you need to get access to the admin panel, you need to run `python manage.py createsuperuser`. This will create an admin in the db, and with those new credentials you will be able to log in.

Start the Django app by running `python manage.py runserver 0.0.0.0:8000`

#### With Docker

A Dockerfile is provided with this repo, as a docker entrypoint which is a script that'll be run each time a container is started.

Before running the container, you need to build the image:

    docker build -t lillijane/django_eps ~/psychic-waffle

When it's built, you can run it with this command:

    docker run -d -p 127.0.0.1:8000:8000 --name eps lillijane/django_eps
It is important to precise the port, especially from the server, because it's the only way to link it with the nginx configuration. Keep in mind that you need to be careful about the data persistance. If you want to keep your data, you can run (by replacing `/home/` by your path to your directory):

    docker run -d -p 127.0.0.1:8000:8000 --name eps   \
        -v /home/db.sqlite3:/usr/src/app/db.sqlite3   \
        -v /home/pic_folder/:/usr/src/app/pic_folder/ \
        -v /home/eps_app/static/img/:/usr/src/app/eps_app/static/img/
        lillijane/django_eps

### API documentation

To use the chatterbot API, you need to send:

`curl -H "Accept: application/json" \
     -H "Content-Type: application/json" \
     -X POST 'api.talkingstatues.xyz/api/chatterbot/' \
     -d "{'text': 'YOUR MESSAGE'}"`

To receive:

`{
  "text": "Is it true that you are a computer program",
  "created_at": "2017-05-11T10:11:27.085Z",
  "extra_data": {},
  "in_response_to": []
}`

Further documentation on getting set up with Django and ChatterBot can be
found in the `ChatterBot documentation`.

* [Django](https://www.djangoproject.com)
* [ChatterBot](https://github.com/gunthercox/ChatterBot)
* [ChatterBot documentation](http://chatterbot.readthedocs.io/en/latest/django.html)
