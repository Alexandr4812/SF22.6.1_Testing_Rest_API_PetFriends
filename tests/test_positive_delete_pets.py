from app import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import pytest
from settings import log_api, generate_string, russian_chars, chinese_chars, special_chars

pf = PetFriends()

#                     ТЕСТЫ УДАЛЕНИЯ ПИТОМЦА С ПОЗИТИВНЫМ СЦЕНАРИЕМ
###########################################################################################
@log_api
@pytest.mark.api
@pytest.mark.event
def test_delete_pet(get_key):
    '''Проверяем возможность удаления питомца
    + используется фикстура для получения key'''
    #_, api_key = pf.get_app_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(get_key, 'my_pets')

    if len(my_pets['pets']) == 0:
        pf.add_new_pets(get_key, 'Murzik', 'cat', '5', 'images/Fedor.jpg')
        _, my_pets = pf.get_list_of_pets(get_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']

    status, _ = pf.delete_pets(get_key, pet_id)
    _, my_pets = pf.get_list_of_pets(get_key, 'my_pets')

    #assert status == 200
    assert pet_id not in my_pets.values()
    return status, _, get_key