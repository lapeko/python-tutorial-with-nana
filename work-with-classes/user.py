class User:
    def __init__(self, full_name, email, password, job):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.job = job

    def print_it(self):
        print(f"User. Full name: {self.full_name}. Email: {self.email}. Password: {self.password}. Job: {self.job}.")
