class Product:
    def __init__(self, name, price, amount, is_active, _id):
        self.id = _id        
        self.name = name
        self.price = price
        self.amount = amount
        self.is_active = is_active

all_products = []
id = 1  # Global id başlangıç değeri
        
def add_product():
    global id
    p_name = input("Enter the product name: ")
    p_price = float(input("Enter the product price: "))
    p_amount = int(input("Enter the product amount: "))
    p_active = int(input("Enter (0 or 1) for active status: "))
    
    product = Product(p_name, p_price, p_amount, p_active, id)
    all_products.append(product)
    id += 1
    
    print(f"Product {p_name} added successfully!")
    print("Current product list:")
    for p in all_products:
        print(f"ID: {p.id}, Name: {p.name}, Price: {p.price}, Amount: {p.amount}, Active: {p.is_active}")

def show_product():
    if not all_products:
        print("No products available.")
        return
    for product in all_products:
        print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Amount: {product.amount}, Active: {product.is_active}")
      
def delete_product():
    show_product()
    del_id = int(input("Enter the ID of the product to delete: "))
    global all_products
    all_products = [p for p in all_products if p.id != del_id]
    print(f"Product with ID {del_id} has been deleted.")
      
def update_product():
    show_product()
    up_id = int(input("Enter the ID of the product to update: "))
    for product in all_products:
        if product.id == up_id:
            product.name = input(f"Enter new name for product (current: {product.name}): ") or product.name
            product.price = float(input(f"Enter new price for product (current: {product.price}): ") or product.price)
            product.amount = int(input(f"Enter new amount for product (current: {product.amount}): ") or product.amount)
            product.is_active = int(input(f"Enter new active status (0 or 1) (current: {product.is_active}): ") or product.is_active)
            print(f"Product with ID {up_id} has been updated.")
            return
    print(f"No product found with ID {up_id}.")

while True:
    print("""
    1. Add
    2. Show
    3. Remove
    4. Update
    else: Exit program
    """)
    try:
        command = int(input("Enter the command: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if command == 1:
        add_product()
    elif command == 2:
        show_product()
    elif command == 3:
        delete_product()
    elif command == 4:
        update_product()
    else:
        print("Exiting Program!!!")
        break
