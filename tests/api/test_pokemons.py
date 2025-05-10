import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b4a5083d63e0759743e7f4204c0dcbba'
HEADER = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {TOKEN}',
    'trainer_token' : TOKEN}
TRAINER_ID = '30421'


def test_status_code():
    response = requests.get(
        url = f'{URL}/pokemons',
        params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(
        url = f'{URL}/pokemons',
        params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == "koko"

def test_list_of_trainers():
    response = requests.get(
        url = f'{URL}/trainers',
        params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200


@pytest.mark.parametrize('key, value', [
    ('name', 'koko'),
    ('trainer_id', TRAINER_ID),
     ('id', '305971')])
def test_parametrieze(key, value):
    response_parametrize = requests.get(
        url = f'{URL}/pokemons',
        params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value