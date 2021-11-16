from app import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import pytest
from settings import log_api, generate_string, russian_chars, chinese_chars, special_chars

pf = PetFriends()

#                     ТЕСТЫ СОЗДАНИЯ ПИТОМЦЕВ С ПОЗИТИВНЫМ СЦЕНАРИЕМ
###########################################################################################

@log_api
@pytest.mark.api
@pytest.mark.event
def test_add_pets_with_valid_data(get_key,name='Fedor', animal_type='cat', age='3', pet_photo='images/Fedor.jpg'):
    '''Проверяем что код статуса запроса 200 и что список с добавленными данными не пустой для этого
    в переменную pet_photo сохраняем путь к файлу фотографии питомца,
    проверяем статус ответа и что в ответе содержатся добавленные данные.
    + используется фикстура для получения key и статуса ответа key.
     '''
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    #_, api_key = pf.get_app_key(valid_email, valid_password)
    status, result = pf.add_new_pets(get_key, name, animal_type, age, pet_photo)
    #assert status == 200
    assert result['name'] == name
    return status, result, get_key, name, animal_type, age, pet_photo

###############################################################################################

@log_api
@pytest.mark.api
@pytest.mark.event
def test_add_pets_with_valid_data_without_photo(get_key, name='МурзикБезФото', animal_type='кот', age='6'):
    '''Проверяем возможность добавления нового питомца без фото
    + используется фикстура для получения key и статуса ответа key'''
    status, result = pf.add_new_pet_without_photo(get_key, name, animal_type, age)
    #assert status == 200
    assert result['name'] == name
    return status, result, get_key, name, animal_type, age

################################################################################################

@pytest.mark.parametrize("name", [
   ''
   , generate_string(255)
   , generate_string(1001)
   , russian_chars()
   , russian_chars().upper()
   , chinese_chars()
   , special_chars()
   , '123'
], ids=[
   'empty'
   , '255 symbols'
   , 'more than 1000 symbols'
   , 'russian'
   , 'RUSSIAN'
   , 'chinese'
   , 'specials'
   , 'digit'
])
@pytest.mark.parametrize("animal_type", [
   ''
   , generate_string(255)
   , generate_string(1001)
   , russian_chars()
   , russian_chars().upper()
   , chinese_chars()
   , special_chars()
   , '123'
], ids=[
   'empty'
   , '255 symbols'
   , 'more than 1000 symbols'
   , 'russian'
   , 'RUSSIAN'
   , 'chinese'
   , 'specials'
   , 'digit'
])
@pytest.mark.parametrize("age", [
    '1'
], ids=[
    'min'])
@log_api
@pytest.mark.api
@pytest.mark.event
def test_add_pets_with_different_parameters(get_key, name, animal_type, age):
    '''Проверяем возможность добавления нового питомца без фото с различным
    типами данных проверки корректности обработки API сервера
    + используется фикстура для получения key и статуса ответа key'''
    status, result = pf.add_new_pet_without_photo(get_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
    assert result['age'] == age
    assert result['animal_type'] == animal_type
    return status, result, get_key, name, animal_type, age