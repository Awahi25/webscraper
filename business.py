class Business:
    def __init__(self, name, address, phone_number, email, website):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.website = website

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nWebsite: {self.website}\n"
