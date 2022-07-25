from django.core.management.base import BaseCommand
from django.db.models import Q

from apps.nomenclator.models import Municipality, Location, Country
import json


class Command(BaseCommand):
    """ New command to populate database"""

    def handle(self, *args, **options) -> None:
        try:
            file_data = open("seed/provincias.txt")
            provinces = json.load(file_data)['provinces']
            file_data.close()
            file_data = open("seed/municipios.txt")
            municipalities = json.load(file_data)['cities']
            file_data.close()
            country = Country.objects.get(pk=1)
            for province in provinces:
                pk = int(province['region'])
                if not Location.objects.filter(Q(pk=pk) | Q(name=province['city'])):
                    Location.objects.create(pk=pk, name=province['city'], country=country)
                else:
                    location = Location.objects.get(Q(pk=pk) | Q(name=province['city']))
                    location.pk = pk
                    location.name = province['city']
                    location.country = country
                    location.save()
            for municipality in municipalities:
                try:
                    pk = int(municipality['region'])
                    region = Location.objects.get(pk=pk)
                    if not Municipality.objects.filter(name=municipality['city'], location=region):
                        Municipality.objects.create(name=municipality['city'], location=region)
                except:
                    print('error', municipality)


        except Exception as e:
            print("Command complete with errors: {}".format(str(e)))
