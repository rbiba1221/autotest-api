import httpx

loggin_payload = {
    "email": "user@example.com",
    "password": "1221"
}

loggin_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=loggin_payload)
response_loggin = loggin_response.json()

print(f'loggin: {response_loggin}')
print(f'Status code: {loggin_response.status_code}')


me_payload_token = {
    "Authorization": f'Bearer {response_loggin["token"]['accessToken']}'
}
print(f'me_payload_token: {me_payload_token}')
response_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=me_payload_token)
response_me_me = response_me.json()

print(f'me: {response_me_me}')
print(f'Status code: {response_me.status_code}')