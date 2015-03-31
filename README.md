**This repository** is a venv containing Sentry and its dependencies, minus compatible dependencies currently available in Debian Jessie.

### Steps to reproduce/update the contents of this venv ###

1. Create a new Debian Jessie VM on labs
2. Install the dependencies listed under "System dependencies" below with apt
3. Create the /srv/deployment/sentry/ folder
4. Go to that folder and run "virtualenv --system-site-packages sentry" to create the venv
5. Run "source sentry/bin/activate" to activate the venv
6. Run "pip install sentry[postgres]" to install the latest version of Sentry and its dependencies into the venv with postgres support
7. Set up git-review in the /srv/deployment/sentry/sentry folder and commit the changes to this repository

### System dependencies ###

The following dependencies are currently (2015-04-01) available as Debian packages in Jessie and meet Sentry 7.4.3's requirements:

python-beautifulsoup
python-cssutils
python-django-crispy-forms
python-django-jsonfield
python-django-picklefield
python-ipaddr
python-mock
python-progressbar
python-pytest
python-redis
python-six
python-setproctitle

python-psycopg2

The machine where this venv is set up to run needs to have the above Devian packages installed, with versions that
meet the requirements declared by Sentry.

### Possible future issues and reasoning ###

It's quite possible that Debian Jessie's packages will be updated and might no longer meet Sentry's requirements.
Updating the venv using the steps outlined above would fix that problem. When the venv gets built, it will see
that the system package doesn't meet the requirements anymore and an appropriate version from pypi will be pulled
and added to the venv.

It's tempting to not use system packages at all and put all the dependencies in the venv, and we might end up doing that.
However the venv has the major drawback of needing manual steps to be updated when security updates are issued, which is
why we've started this by using as many system packages as we can. Long term, the best of both worlds is probably
to go full venv and set up a bot that will update our venvs automatically.