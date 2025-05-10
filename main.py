import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b4a5083d63e0759743e7f4204c0dcbba'
HEADER = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {TOKEN}',
    'trainer_token' : TOKEN
}

body_registration = {
    "trainer_token": TOKEN,
    "email": "Sokolovs@yandex.ru",
    "password": "BkmzzZ6"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "305971",
    "name": "koko",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "305971"
}

# Регистрация
'''response = requests.post(
    url=f'{URL}/trainers/reg',
    headers=HEADER,
    json=body_registration)

print(response.status_code)
print(response.text)'''

# Подтверждение почты
'''response_confirmation = requests.post(
    url = f'{URL}/trainers/confirm_email',
    headers = HEADER, 
    json = body_confirmation)

print(response_confirmation.text)'''

# Создание покемона
'''response_create = requests.post(
    url = f'{URL}/pokemons',
    headers = HEADER, 
    json = body_create)

print(response_create.text)

message = response_create.json()['message']
print(message)'''

# Изменение имени покемона
'''response_change = requests.put(
    url = f'{URL}/pokemons',
    headers = HEADER,
    json = body_change)

print(response_change.text)'''

# Поймать покемона в покебол
response_catch = requests.post(
url = f'{URL}/trainers/add_pokeball',
headers = HEADER,
json = body_catch)

print(response_catch.text)

