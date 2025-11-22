import services 
from inventory import inventory 
import files


def principal_menu():
    inventory_menu = (
    "\n--- Inventory ---\n"
    "1. Add\n"
    "2. Show\n"
    "3. Search\n"
    "4. Update\n"
    "5. Remove\n"
    "6. Statistics\n"
    "7. Save CSV\n"
    "8. Load CSV\n"
    "9. Exit\n"
    )
    option = services.validate_integer(inventory_menu,"Select an option: ", 1, 9)
    return option

while True:
    option = principal_menu()
    
    match option:
    
        case 1:             
            services.add_product(inventory)
    
        case 2: 
            services.show_inventory(inventory)
    
        case 3: 
            services.look_for_product(inventory)
    
        case 4:
            services.update_product(inventory)
        
        case 5:
            services.product_delete(inventory)
    
        case 6:
            services.calculate_statistics(inventory)
    
        case 7:
            files.save_csv(inventory)

    
        case 8:
            files.load_csv(inventory)
        
        case 9:
           print("Thank you for using our services")
           print("Exiting...")
           break


