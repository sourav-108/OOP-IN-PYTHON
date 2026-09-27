class Product:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, customer):
        self.subscribers.append(customer)

    def restock(self):
        for customer in self.subscribers:
            print(f"Notify {customer}: {self.name} is back in stock")


product = Product("Running shoes")
product.subscribe("Maya")
product.subscribe("Leo")
product.restock()