# Импортируем встроенный модуль json для работы с форматом JSON
import json

# Создаем строку в формате JSON, которая содержит объект со свойствами:
# именем, возрастом, статусом студента и списком курсов
json_data = """
{
  "name" : "Ivan",
  "age" : 37,
  "is_student" : true,
  "courses" : [
    "QA","AT",
    {
      "name" : "Aliase"
    }
  ]
}"""

# Десериализация: превращаем JSON-строку в привычный словарь Python (dict)
parse_data = json.loads(json_data)

# Выводим полученный словарь и его тип данных (должен быть <class 'dict'>)
print(parse_data, type(parse_data))

# Обращаемся к элементам словаря по ключам и выводим их значения
print(parse_data['courses'])  # Выведет список курсов
print(parse_data['name'])     # Выведет имя "Ivan"

# Создаем обычный словарь Python с данными другого человека
data = {
    'name' : 'Maria',
    'age' : 18,
    'is_student' : False,
}

# Сериализация: превращаем словарь Python в строку формата JSON
# Параметр indent=4 делает красивый отступ в 4 пробела для читаемости
json_string = json.dumps(data, indent=4)

# Выводим получившуюся JSON-строку и её тип данных (должен быть <class 'str'>)
print(json_string, type(json_string))


# Открываем файл "jsone_example.json" для чтения ("r") в кодировке UTF-8
with open("jsone_example.json", "r", encoding="UTF-8") as file:
    # Читаем JSON-данные напрямую из файла и преобразуем их в объект Python
    read_data = json.load(file)
    # Выводим прочитанные данные в консоль
    print(read_data)


# Открываем файл "jsone_user.json" для записи ("w") в кодировке UTF-8
# Если файла нет, Python создаст его автоматически
with open("jsone_user.json", "w", encoding="UTF-8") as file:
    # Записываем словарь data напрямую в файл в формате JSON с отступами
    json.dump(data, file, indent=4)
