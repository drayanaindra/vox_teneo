## Setup project

clone this project

create and install virtualenv



    $ virtualenv teneo
    
    $ source teneo/bin/activate
    
    $ pip install -r requirements/base.txt


syncdb and migrate

    $ ./manage.py syncdb --settings=vtmember.settings.local
     
    $ ./manage.py migrate --settings=vtmember.settings.local


runserver

    $ ./manage.py runserver --settings=vtmember.settings.local

