from user import User
from post import Post

user1 = User("Vasya", "@", "123", job="Some job")
user1.print_it()

post = Post("Some title", "Content bla bla")
post.print_it()
