

from ..api_client import APIClient
from typing import TypedDict
from httpx import Response, Client



class CreateUserRequest(TypedDict):

    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    def create_user_api(self, request: CreateUserRequest) -> Response:

        return self.post("http://localhost:8000/api/v1/users", json=request)

http_client = Client()
client = PublicUsersClient(client=http_client)
response= client.create_user_api({"email": "u1ser@example.com",
  "password": "st11ring",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"})

print("Статус ответа:", response.status_code)
try:
    print("Детали ошибки от сервера:", response.json())  # <-- Добавляем эту строку
except Exception:
    print("Текст ответа (если не JSON):", response.text)