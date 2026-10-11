subject1 = input("Название первого предмета: ")
lessons1 = int(input(f"Занятий по '{subject1}' в неделю (>= 0): "))
duration1 = int(input(f"Продолжительность одного занятия по '{subject1}' (мин, > 0): "))
 
subject2 = input("Название второго предмета: ")
lessons2 = int(input(f"Занятий по '{subject2}' в неделю (>= 0): "))
duration2 = int(input(f"Продолжительность одного занятия по '{subject2}' (мин, > 0): "))
 
available_hours = float(input("Доступное время в неделю (ч): "))
 
minutes1 = lessons1 * duration1
minutes2 = lessons2 * duration2
total_minutes = minutes1 + minutes2
total_hours = total_minutes / 60
free_hours = available_hours - total_hours
total_4_weeks = total_hours * 4
 
print()
print("=== Учебная нагрузка ===")
print(f"{subject1}: {minutes1} мин/неделю")
print(f"{subject2}: {minutes2} мин/неделю")
print(f"Общая нагрузка:        {total_minutes} мин = {total_hours:.2f} ч")
print(f"Свободное время:       {free_hours:.2f} ч")
print(f"Нагрузка за 4 недели:  {total_4_weeks:.2f} ч")
