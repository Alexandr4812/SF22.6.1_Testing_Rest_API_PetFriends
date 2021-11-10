from app import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import pytest
from settings import log_api, generate_string, russian_chars, chinese_chars, special_chars

pf = PetFriends()

#                     ТЕСТЫ ДОБАВЛЕНИЯ ФОТО ПИТОМЦЕВ С ПОЗИТИВНЫМ СЦЕНАРИЕМ
###########################################################################################

@log_api
@pytest.mark.ui
@pytest.mark.event
def test_add_photo_at_pet(get_key, pet_photo='images/German.jpg'):
    '''Проверяем возможность добавления новой фотографии питомца
    + используется фикстура для получения key'''
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    #_, api_key = pf.get_app_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(get_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(get_key, my_pets['pets'][0]['id'], pet_photo)
        _, my_pets = pf.get_list_of_pets(get_key, 'my_pets')
        #assert status == 200
        assert result['pet_photo'] == my_pets['pets'][0]['pet_photo']
    else:
        raise Exception("Питомцы отсутствуют")
    return status, result, get_key, pet_photo