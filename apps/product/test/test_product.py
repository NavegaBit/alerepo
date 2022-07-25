from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.conf import settings

class ProductsViewTest(APITestCase):

    def setUp(self) -> None:
        """
        Function set data for the test
        :return: None
        """
        settings.DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'dbhad4lrom3b6e',
                'USER': 'zqgeehefiqngkr',
                'PASSWORD': 'efc9d8d677f69e3b8cc3cc7563cfa3da0541766dbd68c7a3e195b6594cfd8d5a',
                'HOST': 'ec2-34-231-177-125.compute-1.amazonaws.com',
                'PORT': '5432',
            }
        }

    def tearDown(self) -> None:
        """
        Function set data for the test
        :return: None
        """
        pass

    def test_create_function(self) -> None:
        pass