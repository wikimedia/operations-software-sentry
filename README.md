**This repository** is a venv containing Sentry and its dependencies, minus compatible dependencies currently available in Debian Jessie.

### Steps to reproduce/update the contents of this venv ###

1. Create a new Debian Jessie VM on labs
2. Install the virtualenv package
3. Install the dependencies listed under "System dependencies" below with apt
4. Create the /srv/deployment/sentry/ folder
5. Go to that folder and run "virtualenv --system-site-packages sentry" to create the venv
6. Run "source sentry/bin/activate" to activate the venv
7. Run "pip install sentry[postgres]" to install the latest version of Sentry and its dependencies into the venv with postgres support
8. Run "virtualenv --relocatable sentry" to rewrite the file references to relative
9. Copy the extra files from the repo (TODO: these should probably be in a separate project or branch): README.md list-debian-packages.py requirements_list.py requirements_map.py
10. Set up git-review in the /srv/sentry folder and commit the changes to this repository

### System dependencies ###

The following dependencies are currently (2015-07-30) available as Debian packages in Jessie and meet Sentry 7.7.0's requirements:

* python-beautifulsoup
* python-celery
* python-cssutils
* python-django-crispy-forms
* python-django-jsonfield
* python-django-picklefield
* python-ipaddr
* python-mock
* python-progressbar
* python-psycopg2
* python-pytest
* python-dateutil
* python-redis
* python-six
* python-setproctitle

The machine where this venv is set up to run needs to have the above Devian packages installed, with versions that
meet the requirements declared by Sentry.

Additional packages that are not required for running Sentry but needed to build some of the pip packages:
* gcc
* python-dev
* libxml2-dev
* libxslt1-dev
* libffi-dev
* libssl-dev

list-debian-packages.py can help with the updating of the dependency list.

### Possible future issues and reasoning ###

It's quite possible that Debian Jessie's packages will be updated and might no longer meet Sentry's requirements.
Updating the venv using the steps outlined above would fix that problem. When the venv gets built, it will see
that the system package doesn't meet the requirements anymore and an appropriate version from pypi will be pulled
and added to the venv.

It's tempting to not use system packages at all and put all the dependencies in the venv, and we might end up doing that.
However the venv has the major drawback of needing manual steps to be updated when security updates are issued, which is
why we've started this by using as many system packages as we can. Long term, the best of both worlds is probably
to go full venv and set up a bot that will update our venvs automatically.
