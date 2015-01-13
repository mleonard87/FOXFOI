FOXFOI
======

Freedom of Information project written in Django

Development Setup
-----------------
1. Install git and [Vagrant](https://docs.vagrantup.com).
2. Clone this repository.
3. Create a file called `foxfoi/settings/secrets.json` with the configuration found in the "secrets.json" section below.
4. Run `vagrant up` from your working copy (this may take some time as it downloads the necessary dependences).
5. SSH to your Vagrant VM with `vagrant ssh`.
6. Start the development server with `/vagrant/manage.py runserver 0.0.0.0:8000`. Note: Specifying the ip range of 0.0.0.0 ensures that the host will be able to communicate with the Django development server.
7. Point your browser at localhost:8090.

secrets.json
------------
```
{
  "DB_NAME": "",
  "DB_USERNAME": "",
  "DB_PASSWORD": "",
  "SECRET_KEY": "",
  "SOCIAL_AUTH_GOOGLE_OAUTH2_KEY": "",
  "SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET": ""
}
```