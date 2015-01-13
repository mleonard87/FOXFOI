FOXFOI
======

Freedom of Information project written in Django

Development Setup
-----------------
1. Install git and [Vagrant](https://docs.vagrantup.com).
2. Clone this repository.
3. Create a file called `foxfoi/settings/secrets.json` with the configuration found in the "secrets.json" section below.
4. Run `vagrant up` from your working copy.
5. Point your browser to `localhost:18090` for running FOXFOI through apache or run `vagrant ssh`, `/vagrant/manage.py runserver 0.0.0.0:8000` and point your browser to `localhost:8090`.

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