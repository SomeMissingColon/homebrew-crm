import db_util
class Prospect():
    def __init__(self,name,telephone,address,website,email,intelligence):
        self.name = name
        self.telephone = telephone
        self.address = address
        self.website = website
        self.email = email
        self.intelligence = intelligence

    def update(self):
        prefix = "  "
        suffix = ()
        db_util.cursor()

