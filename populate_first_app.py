import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()


import random
from first_app.models import AccessRecord,Topic,Webpage

from faker import Faker
fake= Faker()
topics= ['Search','Social','Marketpalce','news','games']

def add_topics():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):
        top = add_topics()

        #creare the fake data for that entry
        fake_url = fake.url()
        fake_date=fake.date()
        fake_name = fake.company()
        
        #create the webpage entry
        webpg= Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("populating...")
    populate(20)
    print("population complete.")