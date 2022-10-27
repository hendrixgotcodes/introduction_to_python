customer= {
    "name": "Samuel",
    "email": "jsmith2@xitroo.com",
    "age": 32,
    "isVerified": True
}

print(customer)
print(customer.get("name"))
print(customer.get("non-existent-key", "default goes here"))

customer["name"] = "Jack Pint"