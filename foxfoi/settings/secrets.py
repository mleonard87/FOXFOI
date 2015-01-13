import os, json, sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def raise_configuration_exception(message):
    if __name__ == '__main__':
        raise Exception(message)
    else:
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured(message)

def get_secret_json(setting, default=None):
    """Get the secret variable of return an explicit exception"""
    try:
        return secrets_json[setting]
    except KeyError:
        if default:
            return default
        error_msg = "Set the {0} property in secrets.json".format(setting)
        raise_configuration_exception(error_msg)

def get_secret_env(setting, default=None):
    """Get the secret variable of return an explicit exception"""
    try:
        return os.environ[setting]
    except KeyError:
        if default:
            return default
        error_msg = "Set the {0} property in an environment variable".format(setting)
        raise_configuration_exception(error_msg)

get_secret = None
if os.path.isfile(os.path.join(BASE_DIR, 'settings', 'secrets.json')):
    with open(os.path.join(BASE_DIR, 'settings', 'secrets.json')) as f:
        secrets_json = json.loads(f.read())
    get_secret = get_secret_json
else:
    get_secret = get_secret_env

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print get_secret(sys.argv[1], sys.argv[2])
    else:
        print get_secret(sys.argv[1])