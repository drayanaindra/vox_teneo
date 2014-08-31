from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

STATUS = (
    ('mn', 'Menikah'),
    ('jl', 'Jomblo')
)

PROGRAMMING = (
    ('py', 'Python'),
    ('rb', 'Ruby'),
    ('pl', 'Perl')
)

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    skill_programming = models.CharField(choices=PROGRAMMING, max_length=2)
    status = models.CharField(choices=STATUS, max_length=2)
