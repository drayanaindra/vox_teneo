## Setup and Instalaton  Project

### Linux/Unix

create and install virtualenv

    $ virtualenv teneo

    $ source teneo/bin/activate

    $ pip install -r requirements/base.txt


### Windows

Following this instalation pip and virtualenv: [Install PIP and virtualenv](http://www.tylerbutler.com/2012/05/how-to-install-python-pip-and-virtualenv-on-windows-with-powershell/)

syncdb and migrate

    $ ./manage.py syncdb --settings=vtmember.settings.local

    $ ./manage.py migrate --settings=vtmember.settings.local


runserver

    $ ./manage.py runserver --settings=vtmember.settings.local
    




