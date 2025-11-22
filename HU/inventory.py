import csv

with open("inventory.csv", "r") as inventory:
    reader = csv.DictReader(inventory)
    for position in reader:
        print(position)



with open("nuevo.csv", "w", newline="") as f:
    campos = ["nombre", "edad"]
    escritor = csv.DictWriter(f, fieldnames=campos)

    escritor.writeheader()  

    escritor.writerow({"nombre": "Ulith", "edad": 20})