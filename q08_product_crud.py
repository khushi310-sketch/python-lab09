products = {}

# Create
products[1] = {"name": "Laptop", "price": 50000}
products[2] = {"name": "Mouse", "price": 500}

# Read
print("Products:")
for product_id, details in products.items():
    print(product_id, details)

# Update
products[1]["price"] = 55000
print("\nUpdated Product:", products[1])

# Delete
del products[2]
print("\nFinal Products:", products)