import httpx
from tools.fakers import get_random_email

greate_user_payload={

  "email": get_random_email(),
  "password": "1221",
  "lastName": "Takeeva",
  "firstName": "Leni",
  "middleName": "Slavikovna"

}

response_greate_user = httpx.post("http://localhost:8000/api/v1/users", json=greate_user_payload)
response_greate_user_data = response_greate_user.json()

print(response_greate_user_data)
print(response_greate_user.status_code)

login_payload = {

    "email": greate_user_payload['email'],
    "password": greate_user_payload['password']
}

response_login = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
response_login_data = response_login.json()


patch_headers = {
    "Authorization": f'Bearer {response_login_data['token']['accessToken']}'
}

patch_payload = {

    "email": get_random_email(),
    "lastName": greate_user_payload['lastName'],
    "firstName": greate_user_payload['firstName'],
    "middleName": greate_user_payload['middleName']
}

response_update = httpx.patch(f'http://localhost:8000/api/v1/users/{response_greate_user_data['user']['id']}',
                              json=patch_payload, headers=patch_headers)
response_update_data = response_update.json()
print(response_update_data)
print(response_update.status_code)


