"""
TASK: 05 Json Writer Reader

# Do some research into JSON
Prompt user for:
- Name
- Price
- Quantity
Store items into a JSON file with proper formatting
Then allow the user to open and convert to list of dictionaries and output the summary with averages.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import json

def reset_json():
    with open("order.json", "w") as file:
        json.dump({'Online Order': {'Items': []}}, file)

def json_write_new(name, price, quantity):
    with open("order.json", "r") as file:
        loaded = json.load(file)

    loaded['Online Order']['Items'].append({'name': name, 'price': price, 'quantity': quantity})

    with open("order.json", "w") as file:
        json.dump(loaded, file)

def get_items():
    with open("order.json", "r") as file:
        items = json.load(file)
    items = items['Online Order']['Items']

    return items

def avg_price_quan():
    items = get_items()
    price_tot = 0
    quan_tot = 0
    count = len(items)
    for item in items:
        price_tot += item['price']
        quan_tot += item['quantity']

    return price_tot/count, quan_tot/count

def main():
    reset_json()
    print(get_items())
    json_write_new("Chicken", 5.00, 12)
    print(get_items())
    json_write_new("Milk", 2.50, 2)
    print(get_items())
    avg_p, avg_q = avg_price_quan()
    print(f"Average price:\t\t{avg_p}")
    print(f"Average quantity:\t{avg_q}")


if __name__ == "__main__":
    main()
