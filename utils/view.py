class View:

    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def show(self):
        print(self.title)
        print(len(self.title)*"*")
        print(self.content)