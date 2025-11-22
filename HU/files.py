import csv, time
from inventory import inventory 

def save_csv(inventory):
    if inventory:
        with open("HU/inventory.csv", "w", newline="") as inventory_file:
            fields = ["name", "price", "quantity"]
            writer = csv.DictWriter(inventory_file, fieldnames=fields)

            writer.writeheader()  
            for product in inventory:
                writer.writerow(product)
        print("Inventory saved successfully")
    
    if not inventory:
        print("Inventory is empty, cannot save csv")
        time.sleep(5)
    return

def load_csv(inventory):
    try:    
        with open("inventory.csv", "r") as inventory_file:
            reader = csv.DictReader(inventory_file)

            original_fields = ["name", "price", "quantity"]
            if reader.fieldnames != original_fields:
                print("Error at looking for csv header")
                time.sleep(2)
                return
            
            loaded_products = []
            error_count = 0
            
            for row in reader:
                
                if len(row) != 3:
                    error_count += 1
                    continue
                
                try:
                    price = float(row["price"])
                    quantity = int(row["quantity"])
                    
                    if price < 0 or quantity < 0:
                        raise ValueError
                    
                    name = row["name"].strip().lower()

                    loaded_products.append({"name": name, "price": price, "quantity": quantity})
                
                except:
                    error_count += 1
                    continue
    
    except FileNotFoundError:
        print("csv file not found")
        time.sleep(2)
        return
    
    except UnicodeDecodeError:
        print("Error with csv file for the encoding")
        time.sleep(2)
        return
    
    choice = input("Overwrite the inventory? (s/n): ").strip().lower()

    if choice == "s":
        inventory.clear()
        inventory.extend(loaded_products)
        print(f"{len(loaded_products)} products loaded. {error_count} rows skipped.")
    
    else:
        for new_product in loaded_products:
            found = False
            
            for old_product in inventory:
                if new_product["name"] == old_product["name"]:
                    old_product["quantity"] += new_product["quantity"]
                    old_product["price"] = new_product["price"]
                    found = True
                    break
            
            if not found:
                inventory.append(new_product)
        
        print(f"- {len(loaded_products)} products mixedn\- {error_count} rows skipn\ ")
        time.sleep(5)   
