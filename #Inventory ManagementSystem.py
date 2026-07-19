#Inventory ManagementSystem
#Lists
products = []
quantity = []

while True:
    print("\n1. Add Product")
    print("2. Search Product")
    print("3. Update Quantity")
    print("4. Delete Product")
    print("5. Stock Report")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        p = input("Enter product name: ")
        q = int(input("Enter quantity: "))
        products.append(p)
        quantity.append(q)

    elif choice == "2":
        p = input("Enter product name: ")
        if p in products:
            i = products.index(p)
            print("Quantity:", quantity[i])
        else:
            print("Product not found")

    elif choice == "3":
        p = input("Enter product name: ")
        if p in products:
            i = products.index(p)
            quantity[i] = int(input("Enter new quantity: "))
            print("Updated")
        else:
            print("Product not found")

    elif choice == "4":
        p = input("Enter product name: ")
        if p in products:
            i = products.index(p)
            products.pop(i)
            quantity.pop(i)
            print("Deleted")
        else:
            print("Product not found")

    elif choice == "5":
        print("\nStock Report")
        for i in range(len(products)):
            print(products[i], "-", quantity[i])

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")