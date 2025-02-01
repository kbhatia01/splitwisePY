from splitwise.management.commands.commands import Command
from splitwise.models import User
from splitwise.service.splitwiseService import SplitwiseService


class SettleUpUser(Command):

    def __init__(self, service: SplitwiseService):
        self.service = service
        super().__init__()

    def match(self, inputstr: str):
        return inputstr.strip().startswith("SettleUpUser")

    def execute(self, inputstr: str):
        print("start sattling..")

        try:
            user_id = int(inputstr.strip().split(" ")[1])
            user = User.objects.get(pk=user_id)
        except Exception as e:
            print(e)

        txns = self.service.settle_up_user(user_id)

        for txn in txns:
            print(txn)

