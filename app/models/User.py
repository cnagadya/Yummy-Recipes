'''base class for all users'''
class User:
    '''base initizialization function'''
    def __init__(self, name, password):
        self.Id = range(0, 1000, 1)
        self.Username = name
        self.Password = password

    def get_username(self):
        return self.Username

    def get_password(self):
        return self.Password

