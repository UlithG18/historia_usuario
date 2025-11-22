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

        data = True

    inventory.append({"name": name, "price": price, "quantity": quantity})
    print(f"Product {name} added successfully")

    


def show_inventory(inventory):
        print(inventory)


def look_for_product(inventory, name):
    while True:
        if not name:    
            name = input("Which is the product you are looking for: ").strip().lower()

            if not name:
                print("You need to enter a product")
                continue
        
            if not all(letters.isalnum() or letters.isspace() or letters == "-" for letters in name):
                print("The product cannot contain special characters but hyphens")
                continue

            found = False
            for product in inventory:
                
                if product["name"] == name:
                    print(product)
                    found = True
                    return
            if not found:
                print("There isn't any product with that name") 

look_for_product(inventory, name)
                    



def update_product(inventory, name, new_price=None, new_quantity=None):
    while True:
        name = input("Which is the product you want to update: ")
        
        if not name:
            print("You need to enter a product")
            continue
    
        if not all(ch.isalnum() or ch.isspace() or ch == "-" for ch in name):
            print("The product cannot contain special characters but hyphens")
            continue

        break
    found = False
    for product in range(inventory):
        
        if product["name"] == name:
            found = True
            while True:
                print("\n--- Update menu ---\n1. Name\n2. Price\n3. Quantity\n4. Exit")
                option = validate_integer("What information do you want to change?: ", 1, 4)
            
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
                            return
                
                    case 2:
                        while True:    
                            
                            try:
                                new_price = float(input("What is the new price for this product?: "))
                                break

                            except ValueError:
                                print("Enter a valid value")
                                                            
                        product["price"] = new_price
                        return     
                
                    case 3:
                        new_quantity = validate_integer("What is the new quantity for this product?: ")  
                        product["quantity"] = new_quantity 
                        return   
                
                    case 4:
                        return
    if not found:
        print("There isn't any product with that name") 
    return     
    



# def eliminar_producto(inventario, nombre):

# def calcular_estadisticas(inventario):

