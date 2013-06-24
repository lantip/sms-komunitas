import os
import sys
import site

# Adjust the path below to point to the site-packages of your virtualenv.
site.addsitedir('/home/angkringan/.virtualenvs/angkringan/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/angkringan/gits/sms-komunitas')
sys.path.append('/home/angkringan/gits/sms-komunitas/medkom')

os.environ['DJANGO_SETTINGS_MODULE'] = 'medkom.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
