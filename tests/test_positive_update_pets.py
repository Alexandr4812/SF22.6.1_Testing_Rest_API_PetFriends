from app import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import pytest
from settings import log_api, generate_string, russian_chars, chinese_chars, special_chars

pf = PetFriends()

#                     ТЕСТЫ ИЗМЕНЕНИЯ ДАННЫХ  ПИТОМЦА С ПОЗИТИВНЫМ СЦЕНАРИЕМ
###########################################################################################

@log_api
@pytest.mark.ui
@pytest.mark.event
def test_update_pet_info(get_key, name='из', animal_type='измененный', age='5'):
    '''Проверяем возможность изменения данных питомца
    + используется фикстура для получения key'''
    #_, api_key = pf.get_app_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(get_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(get_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("Питомцы отсутствуют")
    return  status, result, get_key, name, animal_type, age