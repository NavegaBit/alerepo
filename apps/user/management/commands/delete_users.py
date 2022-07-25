from django.core.management.base import BaseCommand
from apps.user.models import UserManagement


class Command(BaseCommand):
    """ New command to populate database"""

    @staticmethod
    def delete_object(object_data) -> None:
        object_data.delete()

    def handle(self, *args, **options) -> None:
        try:
            user = UserManagement.objects.all()
            user.delete()
        except Exception as e:
            print("Command complete with errors: {}".format(str(e)))
