# profile.py — Карточка студента

last_name = input("Фамилия: ")
first_name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст (полных лет, 1–120): "))
subject = input("Любимый предмет: ")
study_hours = float(input("Часов подготовки в неделю (>= 0): "))

age_in_4_years = age + 4
hours_in_4_weeks = study_hours * 4
hours_per_day = study_hours / 7

print()
print("=== Карточка студента ===")
print(f"Полное имя:              {first_name} {last_name}")
print(f"Группа:                  {group}")
print(f"Город:                   {city}")
print(f"Возраст:                 {age} лет")
print(f"Возраст через 4 года:    {age_in_4_years} лет")
print(f"Любимый предмет:         {subject}")
print(f"Подготовка в неделю:     {study_hours:.2f} ч")
print(f"Подготовка за 4 недели:  {hours_in_4_weeks:.2f} ч")
print(f"Среднее в день:          {hours_per_day:.2f} ч")