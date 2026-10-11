order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")
 
item1_name = input("Первая позиция (название): ")
item1_qty = int(input(f"Количество '{item1_name}' (>= 0): "))
item1_price = float(input(f"Цена единицы '{item1_name}' (руб., >= 0): "))
 
item2_name = input("Вторая позиция (название): ")
item2_qty = int(input(f"Количество '{item2_name}' (>= 0): "))
item2_price = float(input(f"Цена единицы '{item2_name}' (руб., >= 0): "))
 
delivery = float(input("Стоимость доставки (руб., >= 0): "))
paid = float(input("Внесённая сумма (руб.): "))
 
item1_total = item1_qty * item1_price
item2_total = item2_qty * item2_price
goods_total = item1_total + item2_total
grand_total = goods_total + delivery
total_qty = item1_qty + item2_qty
change = paid - grand_total
 
print()
print(f"=== {order_name} ===")
print(f"Заказчик: {customer_name}")
print()
print(f"{'Позиция':<25} | {'Кол-во':>6} | {'Цена':>10} | {'Стоимость':>12}")
print("-" * 62)
print(f"{item1_name:<25} | {item1_qty:>6} | {item1_price:>10.2f} | {item1_total:>12.2f}")
print(f"{item2_name:<25} | {item2_qty:>6} | {item2_price:>10.2f} | {item2_total:>12.2f}")
print("-" * 62)
print(f"{'Итого единиц:':<38} {total_qty:>6}")
print(f"{'Товары без доставки:':<38} {goods_total:>12.2f} руб.")
print(f"{'Доставка:':<38} {delivery:>12.2f} руб.")
print(f"{'ИТОГО с доставкой:':<38} {grand_total:>12.2f} руб.")
print(f"{'Внесено:':<38} {paid:>12.2f} руб.")
print(f"{'Сдача:':<38} {change:>12.2f} руб.")
