class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def print_it(self):
        print(f"Post. Title: {self.title}. Content: {self.content}")
