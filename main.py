from management.product_handler import (
    get_product_by_id, get_products_by_type,
    add_product, menu_report, add_product_extra
    )
from management.tab_handler import calculate_tab
from menu import products


required_keys = ("description", "price", "rating", "title", "type")

new_product = {
    "description": "Potatoes sliced and fried",
    "price": 20,
    "rating": 5,
    "title": "French fries",
    "type": "vegetable",
}

table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]


if __name__ == "__main__":
    try:
        print(get_product_by_id(25))
    except TypeError as error:
        print(error.args[0])
    try:
        print(get_products_by_type("vegetable"))
    except TypeError as error:
        print(error.args[0])
    print(add_product(products, **new_product))
    print(calculate_tab(table_1))
    print(menu_report())
    try:
        print(add_product_extra(products, *required_keys, **new_product))
    except KeyError as error:
        print(error.args[0])
