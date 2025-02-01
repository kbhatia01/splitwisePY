from django.core.management import BaseCommand

from splitwise.management.commands.CommandExecutor import CommandExecutor
from splitwise.management.commands.SettleUpUser import SettleUpUser
from splitwise.service.splitwiseService import SplitwiseService


class Command(BaseCommand):

    def __init__(self):
        self.executor = CommandExecutor()
        self.executor.add_command(SettleUpUser(SplitwiseService()))
        super().__init__()

    help = 'Split data into train and test sets'

    def handle(self, *args, **options):
        print('ENTER COMMAND eg SettleUser1')
        while True:
            inputStr = input()

            try:
                self.executor.execute(inputStr)

            except Exception as e:
                print(e)
