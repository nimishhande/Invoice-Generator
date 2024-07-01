def get_invoice_details():
    customer_name = input("Enter customer name: ")
    num_items = int(input("Enter the number of items: "))

    items = []
    for i in range(num_items):
        item_name = input(f"Enter item {i + 1} name: ")
        quantity = int(input(f"Enter quantity for {item_name}: "))
        price = float(input(f"Enter price for {item_name}: "))
        items.append((item_name, quantity, price))

    return customer_name, items

def calculate_total(items):
    total = 0
    for item_name, quantity, price in items:
        total += quantity * price
    return total

def print_invoice(customer_name, items, total):
    print("\nInvoice:")
    print(f"Customer Name: {customer_name}")
    print("Items:")
    for item_name, quantity, price in items:
        print(f"{item_name} ({quantity} x ${price:.2f} each)")
    print(f"Total: ${total:.2f}")

def main():
    print("Welcome to the Invoice Generator!")
    customer_name, items = get_invoice_details()
    total = calculate_total(items)
    print_invoice(customer_name, items, total)

if __name__ == "__main__":
    main()
