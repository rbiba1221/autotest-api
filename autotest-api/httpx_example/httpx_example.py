import httpx  # Импортируем библиотеку HTTPX для работы с HTTP-запросами

# --- 1. Простой GET-запрос для получения данных ---
# Отправляем GET-запрос к API, чтобы получить задачу с ID 1
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

# Выводим HTTP-статус код ответа (например, 200 OK)
print(f'статус код: {response.status_code}')
# Парсим тело ответа из формата JSON в словарь Python и выводим его
print(response.json())


# --- 2. POST-запрос с отправкой JSON-данных ---
# Создаем словарь с данными для новой задачи
data = {
  "userId": 1,
  "title": "Новая задача",
  "completed": False
}

# Отправляем POST-запрос, передавая данные через аргумент json (автоматически сериализует в JSON и ставит нужный Content-Type)
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(f'статус код: {response.status_code}') # Обычно 201 Created
print(response.json())                        # Выводим созданный объект, который вернул сервер
print(response.headers)                       # Выводим заголовки ответа от сервера


# --- 3. POST-запрос с отправкой данных формы (Form Data) ---
# Создаем словарь с данными пользователя
data = { "username": "test_user", "password": "123456"}

# Отправляем POST-запрос, используя аргумент data (передает данные как application/x-www-form-urlencoded)
response = httpx.post("https://httpbin.org/post", data=data)
print(f'статус код: {response.status_code}')
print(response.json())
print(response.headers)


# --- 4. GET-запрос с пользовательскими заголовками (Headers) ---
# Создаем словарь с заголовками (например, для авторизации)
headers = {"autorization": "my jwt token"}
# Отправляем GET-запрос и передаем заголовки в аргумент headers
response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.json())
print(response.request.headers) # Выводим заголовки, которые мы *отправили* в запросе (чтобы проверить отправку токена)


# --- 5. GET-запрос с параметрами строки (URL Query Params) ---
# Создаем словарь с параметрами фильтрации
params = {"userId": 1}
# Отправляем запрос, параметры автоматически превратятся в "?userId=1" в конце URL
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.url)  # Выводим итоговый собранный URL, чтобы убедиться в правильности параметров
print(response.json())


# --- 6. POST-запрос с отправкой файла ---
# Внимание: для работы этого шага в текущей папке должен существовать файл "test.txt"
# Создаем словарь, где ключ — имя поля, а значение — кортеж с именем файла и открытым файловым объектом в бинарном режиме
files = {"file": ("test.txt", open("test.txt", "rb"))}
# Отправляем POST-запрос с файлом (передается как multipart/form-data)
response = httpx.post("https://httpbin.org/post", files=files)
print(f'ответ!!!:{response.json()}')


# --- 7. Использование сессии (Client) через контекстный менеджер `with` ---
# Открываем клиентскую сессию. Это оптимизирует работу (повторно использует TCP-соединения)
with httpx.Client() as client:
  # Делаем запросы через объект client, а не через модуль httpx напрямую
  response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
  response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
# Здесь сессия автоматически закрывается

print(response1.json())
print(response2.json())


# --- 8. Создание преднастроенного Клиента с общими заголовками ---
# Создаем клиента и сразу задаем ему базовые заголовки, которые будут отправляться при *каждом* запросе
client = httpx.Client(headers={"autorization": "my jwt token"})
# Делаем запрос: заголовок авторизации подставится автоматически
response = client.get("https://httpbin.org/get")
print(response.json())
# Не забываем закрывать клиента вручную, если не использовали 'with'
client.close()


# --- 9. Обработка ошибок HTTP-статусов ---
try:
  # Отправляем запрос по заведомо неверному адресу (вернет 404)
  response = httpx.get("https://jsonplaceholder.typicode.com/todos/invalid-uri")
  # Вызываем исключение, если статус-код ответа равен 4xx или 5xx
  response.raise_for_status()
except httpx.HTTPError as e:
  # Перехватываем ошибку HTTP и выводим сообщение о ней
  print(f'ошибка статуса {e}')


# --- 10. Обработка таймаутов (ожидания ответа) ---
try:
  # Эндпоинт /delay/5 искусственно задерживает ответ на 5 секунд.
  # Мы выставляем timeout=5. Если ответ не придет ровно за 5 секунд (или быстрее), случится ошибка.
  response = httpx.get("https://httpbin.org/delay/5", timeout=5)
except httpx.ReadTimeout:
  # Перехватываем ошибку превышения времени ожидания чтения данных
  print('Превышено ожидание')





