import httpx

# Шаг 1: Подготовка данных пользователя для авторизации
login_payload = {
    "email": "user@example.com",
    "password": "1221"
}

# Шаг 2: Отправка POST-запроса на авторизацию (Login)
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

# Шаг 3: Чтение и вывод ответа сервера после входа
response_login_data = login_response.json()
print(f'Login responce: {response_login_data}')
print(f'Status code: {login_response.status_code}')

# Шаг 4: Извлечение refreshToken из полученного ответа для формирования нового payload
refresh_payload = {
    "refreshToken": response_login_data['token']['refreshToken']
}

# Шаг 5: Отправка POST-запроса на обновление токена (Refresh) с использованием refreshToken
refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)

# Шаг 6: Чтение и вывод нового ответа сервера с обновленными токенами
refresh_token_data = refresh_response.json()
print(f'Refresh token responce: {refresh_token_data}')
print(f'Status code: {refresh_response.status_code}')
