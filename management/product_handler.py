from menu import products


def get_product_by_id(product_id: int):
    if type(product_id) is not int:
        raise TypeError("product id must be an int")
    for item in products:
        if item["_id"] == product_id:
            return item
    return {}


def get_products_by_type(product_type: str):
    if type(product_type) is not str:
        raise TypeError("product type must be a str")
    dish_list = []
    for item in products:
        if item["type"] == product_type:
            dish_list.append(item)
    return dish_list


def add_product(menu: list, **kwargs: dict):
    bigger_product_id = 0
    for product in menu:
        if product["_id"] > bigger_product_id:
            bigger_product_id = product["_id"]
    new_id = bigger_product_id + 1
    new_product = kwargs
    new_product["_id"] = new_id
    menu.append(new_product)
    return new_product


def menu_report():
    product_count = len(products)

    all_products_sum = sum(product["price"] for product in products)

    average = round(all_products_sum / product_count, 2)

    type_counts = {}
    for product in products:
        type_counts[product["type"]] = type_counts.get(product["type"], 0) + 1
    most_common_type = max(type_counts, key=type_counts.get)

    string = (
        f"Products Count: {product_count} - "
        f"Average Price: ${average} - Most Common Type: {most_common_type}"
        )
    return string


def add_product_extra(menu: list, *required: tuple, **new_item: dict):
    for key in required:
        if key not in new_item.keys():
            raise KeyError(f"Field '{key}' is required")
    bigger_product_id = 0
    for product in menu:
        if product["_id"] > bigger_product_id:
            bigger_product_id = product["_id"]
    new_id = bigger_product_id + 1
    new_product = new_item
    new_product["_id"] = new_id
    menu.append(new_product)
    return new_product
