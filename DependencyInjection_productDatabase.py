class ProductDatabase:
    def find_product(self, product_id):
        return {"id": product_id, "name": "Lamp"}


class ProductService:
    def __init__(self, database):
        self.database = database

    def get_product_name(self, product_id):
        product = self.database.find_product(product_id)
        return product["name"]


database = ProductDatabase()
service = ProductService(database)
print(service.get_product_name(12))