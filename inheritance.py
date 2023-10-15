class Console:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"{self.name}")

class Xbox(Console):
    def info(self):
        print