from app import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import pytest
from settings import log_api, generate_string, russian_chars, chinese_chars, special_chars

pf = PetFriends()

#                     ТЕСТЫ СОЗДАНИЯ ПИТОМЦЕВ С НЕГАТИВНЫМ СЦЕНАРИЕМ
###########################################################################################

@pytest.mark.parametrize("name", [''], ids=['empty'])
@pytest.mark.parametrize("animal_type", [''], ids=['empty'])
@pytest.mark.parametrize("age",[
    '',
    '-1',
    '0',
    '100',
    '1.5',
    '2147483647',
    '2147483648',
    special_chars(),
    russian_chars(),
    russian_chars().upper(),
    chinese_chars()]
   , ids=[
        'empty',
        'negative',
        'zero',
        'greater than max',
        'float',
        'int_max',
        'int_max + 1',
        'specials',
        'russian',
        'RUSSIAN',
        'chinese'])
@log_api
@pytest.mark.api
@pytest.mark.event
def test_add_pets_with_negative_parameters(get_key, name, animal_type, age):
    '''Проверяем возможность добавления нового питомца без фото с различным
    типами негативных данных. Проверяем что статус ответа 400 а не 500 и не 200
    + используется фикстура для получения key и статуса ответа key'''
    status, result = pf.add_new_pet_without_photo(get_key, name, animal_type, age)
    assert status == 400
    return status, result, get_key, name, animal_type, age