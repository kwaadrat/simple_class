class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def info(self):
        return f"{self.name} (located in {self.location})"
    
class Product:
    def __init__(self, name, price, company):
        self.name = name
        self.price = price
        self.company = company

    def print_info(self):
        print(f"{self.name} is produced by {self.company}")

company = Company("Apple", "California")
product = Product("iPhone", 222, company)

product.print_info()