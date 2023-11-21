# Write your solution here:
# def sort_by_remaining_stock(items: list):
#     return items[2]


# if __name__ == "__main__":
#     products = [
#         ("banana", 5.95, 12),
#         ("apple", 3.95, 3),
#         ("orange", 4.50, 2),
#         ("watermelon", 4.95, 22),
#     ]
#     products.sort(key=sort_by_remaining_stock)
#     for product in products:
#         print(f"{product[0]} {product[2]} pcs")


# def sort_by_remaining_stock(items: list):
#     sorted_items = sorted(items, key=lambda x: x[2])
#     return sorted_items
def sort_by_remaining_stock(items: list):
    def order_by_remaining_stock(item: tuple):
        return item[2]

    return sorted(items, key=order_by_remaining_stock)


if __name__ == "__main__":
    products = [
        ("banana", 5.95, 12),
        ("apple", 3.95, 3),
        ("orange", 4.50, 2),
        ("watermelon", 4.95, 22),
    ]

    for product in sort_by_remaining_stock(products):
        print(f"{product[0]} {product[2]} pcs")
