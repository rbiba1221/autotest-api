import httpx   #создание пользователя через апи ,c генерацией email
from tools.fakers import get_random_email  #импорт сгенерированного Email

payload={

    "email": get_random_email(),
    "password": "1221",
    "lastName": "rbiba",
    "firstName": "d",
    "middleName": "lososb"

}

response = httpx.post("http://localhost:8000/api/v1/users", json=payload)
response_data=response.json()

print(response_data)
print(response.status_code)
