class Product:
    product_count = 0  # Статичне поле для підрахунку кількості створених продуктів

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.product_count += 1

    def display_info(self):
        print(f"Назва продукту: {self.name}")
        print(f"Ціна: {self.price} грн")
        print(f"Загальна кількість створених продуктів: {Product.product_count}")


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period

    def display_info(self):
        super().display_info()
        print(f"Гарантійний термін: {self.warranty_period} місяців")


class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Розмір: {self.size}")


# Приклад використання:
if __name__ == "__main__":
    ep = ElectronicProduct("Ноутбук", 25000, 24)
    cp = ClothingProduct("Футболка", 500, "L")
    
    print("Інформація про електронний продукт:")
    ep.display_info()
    
    print("\nІнформація про одяг:")
    cp.display_info()
