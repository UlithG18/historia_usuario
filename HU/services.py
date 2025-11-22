import os
import time

def restart():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_name(menu, message):
    while True:  
        print(menu)
        name = input(message).strip().lower()

        if not name:
            print("You need to enter a product")
            continue

        if not all(letters.isalnum() or letters.isspace() or letters == "-" for letters in name):
            print("The product cannot contain special characters but hyphens")
            continue
        return name

def validate_integer(menu, message, min=None, max=None):
    while True:
        print(menu)
        try:
            value = int(input(message).strip())
            if min is not None and value < min or max is not None and value > max:
                raise ValueError
            return value
        except ValueError:
            print("Invalid option, enter a valid menu option\n")

def add_product(inventory, name=None, price=None, quantity=None):
    data = False
    while not data:
        
        if not name:    
            name = validate_name("", "\nWhich product do you want to register?: ")

        if price is None:
            try:
                price = float(input("\nWhich price do the product have?: "))
                
                if not price:
                    print("\nThe product's price cannot be empty")
                    continue
  
            except ValueError:
                print("\nYou need to entener a valid value")
                price = 0
                continue

        if price <= 0:
            print("\nThe product's price must be greater than 0")
            price = 0
            continue
            
        if quantity is None:          
            quantity = validate_integer("","\nHow many products are you going to register?: ")

        data = True

    inventory.append({"name": name, "price": price, "quantity": quantity})
    print(f"Product {name} added successfully")
    time.sleep(4)

    


def show_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        time.sleep(2)
        return

    print("\n--- Inventory ---\n")
    
    for product in inventory:
        print(f"Name: {product['name']}")
        print(f"Price: ${product['price']}")
        print(f"Quantity: {product['quantity']}")
    
    time.sleep(10)
    return


def look_for_product(inventory, name=None):
    while True:
        if not name:    
            name = validate_name("", "Which is the product you are looking for: ")

        found = False
        for product in inventory:
            
            if product["name"] == name:
                print("Product found successfully: \n", product)
                time.sleep(5)
                found = True
                return
        if not found:
            print("There isn't any product with that name")
            time.sleep(4)


def update_product(inventory, name=None, new_price=None, new_quantity=None):
    while True:
        if not name:    
            name = validate_name("", "Which is the product you want to update: ")
        
        break
    
    found = False
    for product in inventory:
        
        if product["name"] == name:
            found = True
        
            print("\n--- Update menu ---\n1. Name\n2. Price\n3. Quantity\n4. Exit")
            option = validate_integer("", "What information do you want to change?: ", 1, 4)
        
            match option:
            
                case 1:
                    while True:
                        new_name = input("How do you want to rename this product").strip().lower()

                        if not new_name:
                            print("The product's name cannot be empty")
                            continue

                        if not all(ch.isalnum() or ch.isspace() or ch == "-" for ch in new_name):
                            print("The product only contains letters, spaces or hyphens")
                            continue
                    
                        
                        product["name"] = new_name
                        print("Product name changed successfully")
                        time.sleep(4)
                        return
            
                case 2:
                    while True:     
                        try:
                            new_price = float(input("What is the new price for this product?: "))
                            break

                        except ValueError:
                            print("Enter a valid value")
                                                        
                    product["price"] = new_price
                    print("Product price changed successfully")
                    time.sleep(4)
                    return     
            
                case 3:
                    new_quantity = validate_integer("", "What is the new quantity for this product?: ")  
                    product["quantity"] = new_quantity 
                    print("Product quantity changed successfully")
                    time.sleep(4)
                    return   
            
                case 4:
                    print("Exiting...")
                    time.sleep(2)
                    return
    if not found:
        print("There isn't any product with that name") 
        time.sleep(2)
    return     
    

def product_delete(inventory, name=None):

    while True:
        if not name:    
            name = validate_name("", "Which is the product you want to delete: ")
            break
    
    found = False
    
    for product in inventory:
        if product["name"] == name:
            found = True
            inventory.remove(product)
            print(f"The product {name} has been remove")
            time.sleep(4)
            return
    
    if not found:
        print("There isn't any product with that name")
        time.sleep(2)

def calculate_statistics(inventory):
    if inventory:
        print("\n--- Statistics menu ---\n")

        total_unities = 0
        for product in inventory:
            total_unities += product["quantity"]

        print(f"Total units in inventory: {total_unities}")
        
        total_value = 0
        total_value = sum(product["price"] * product["quantity"] for product in inventory)
        
        print(f"Total value of inventory: ${total_value}")

# agregar_producto(inventario, nombre, precio, cantidad)
# mostrar_inventario(inventario)
# buscar_producto(inventario, nombre) → retorna el dict o None
# actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)
# eliminar_producto(inventario, nombre)
# calcular_estadisticas(inventario) → retorna tupla/dict con métricas
import time
name = ""
print("\n --- Welcome to your personal inventory --- \n")
print("To exit write Exit\n")

inventory = [
    {"name" : "milk", "price" : 100, "quantity" : 20}
    ]

# def menus():
#     update_menu = ("\n--- Update menu ---\n1. Name\n2. Price\n3. Quantity\n4. Exit")

#     return update_menu


def validate_integer(message, min=None, max=None):
    while True:
        try:
            value = int(input(message).strip())
            if min is not None and value < min or max is not None and value > max:
                raise ValueError
            return value
        except ValueError:
            print("Invalid option, enter a valid menu option\n")

def add_product(inventory, name, price, quantity):
    data = False
    while not data:
        
        if not name:    
            name = input("Which product do you want to register?: ").strip().lower()
        
            if not name:
                print("The product's name cannot be empty")
                continue

            if not all(letters.isalnum() or letters.isspace() or letters == "-" for letters in name):
                print("The product only contains letters, spaces or hyphens")
                continue

        if not price:
            try:
                price = float(input("Which price do the product have?: "))
                
                if not price:
                    print("The product's price cannot be empty")
                    continue
  
            except ValueError:
                print("You need to entener a valid value")
                price = 0
                continue

        if price <= 0:
            print("The product's price must be greater than 0")
            price = 0
            continue
            
        if not quantity:          
            quantity = validate_integer("How many products are you going to register?: ")


        exp_product = inventory[0] 
        for product in inventory[1:]:     
            if product["price"] > exp_product["price"]:
                exp_product = product  
        
        print(f"The most expensive product: {exp_product['name']} | ${exp_product['price']}")
        
        
        high_stock = inventory[0]
        for product in inventory[1:]:
            if product["quantity"] > high_stock["quantity"]:
                high_stock = product

        print(f"The highest stock product: {high_stock['name']} | {high_stock['quantity']}")

        sub_total = lambda product: product["price"] * product["quantity"]
        for product in inventory:
            print(f"The subtotal of the product: {product['name']} | ${sub_total(product)}")
        time.sleep(10)
        return
    
    if not inventory:
        print("Inventory is empty.")
        time.sleep(4)
    return

