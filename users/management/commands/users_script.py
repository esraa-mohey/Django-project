from users.models import *
from django.core.management import BaseCommand
from rest_framework import status
import time #To test time related functions
import requests
from django.utils import timezone


class Command(BaseCommand):
    def create_user(self):
        body_json = {
            "username" : "Nasser",
            "password": "nasserPassword",
            "email" : "abdelnasser.ahmed@teqneia.com",
            "first_name" : "Abdelnasser",
            "last_name" : "Ismaiel",
            "middle_Name": "Ahmed",
            "gender" : "M",
            "is_active" : "True",
            "date_of_Birth" : "1996-07-16",
            "country" : 1,
            "typeofidentification" : 1,
            "Number_of_identification" : "12345678915",
            "Home_address": "Sheikh Zayed",
            "typeOfAccount" : 1,
            "mobile" : "012345679885"
        }
        r = requests.post("http://127.0.0.1:8000/users/create/", data = body_json)
        print(r.text)


    def handle(self, *args, **options):
        self.create_user()