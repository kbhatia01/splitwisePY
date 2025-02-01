class CommandExecutor:

    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute(self, inputstr: str):
        for command in self.commands:
            if command.match(inputstr):
                command.execute(inputstr)

        raise Exception("invalid command..")
