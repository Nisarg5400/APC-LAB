products27 = {"Pen": 50, "Pencil": 8, "Eraser": 5, "Book": 20}
products27["Marker"] = 15
products27["Pencil"] = 12

products27.pop("Eraser")

search_product = "Book"
if search_product in products27:
    print(search_product, "quantity:", products27[search_product])



print("Products with quantity below 10:")
for name, qty in products27.items():
    if qty < 10:
        print(name, ":", qty)