import os
import django
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pro2.settings')
django.setup()


# Import settings

import random
from app2.models import user
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # Create new User Entry
        fol = user.objects.get_or_create(First=fake_first_name,Last=fake_last_name,Email=fake_email)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
