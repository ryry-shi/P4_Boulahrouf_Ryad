import os


class View:

    def __init__(self, title: str, content: str = "", blocking: bool = False):
        self.title = title
        self.content = content
        self.blocking = blocking

    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- " + self.title + " ---")
        print()
        if self.content:
            print(self.content)
        if self.blocking:
            input()
