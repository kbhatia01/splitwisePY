from abc import ABC

from django.core.management import BaseCommand


class Command(ABC):

    def match(self, input):
        pass

    def execute(self, input):
        pass