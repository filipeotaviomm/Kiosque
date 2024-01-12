from menu import products


def calculate_tab(orders: list):
    price = 0
    for product in products:
        for order in orders:
            if product["_id"] == order["_id"]:
                price += product["price"] * order["amount"]
    final_price = f"${round(price, 2)}"
    return {"subtotal": final_price}
