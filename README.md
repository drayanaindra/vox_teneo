## Setup project

clone this project

create and install virtualev



    $ virtualenv teneo
    
    $ source teneo/bin/activate
    
    $ pip install -r requreiemtns/base.txt


syncdb and migrate

    $ ./manage.py syncdb --settings=vtmember.settings.local
     
    $ ./manage.py migrate --settings=vtmember.settngs.local


runserver

    $ ./manage.py runserver --settings=vtmember.settings.local

