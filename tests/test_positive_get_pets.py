from app import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import pytest
from settings import log_api, generate_string, russian_chars, chinese_chars, special_chars

pf = PetFriends()


#                     ТЕСТЫ ЗАПРОСОВ О ПИТОМЦАХ С ПОЗИТИВНЫМ СЦЕНАРИЕМ
###########################################################################################

@pytest.mark.parametrize("filter", ['', 'my_pets'], ids= ['empty string', 'only my pets'])
@log_api
@pytest.mark.ui
@pytest.mark.event
def test_get_all_pets_with_valid_key(get_key, filter):
    '''Проверяем что код статуса запроса 200 и список (всех питомцев) или (моих питомцев) не пустой
    с использованием фикстуры и позитивных параметров фильтра. • Заголовок ответа содержит:
    Обязательно - Content-type: aplication/json или application/xml'''
    status, result, responce_headers = pf.get_list_of_pets(get_key, filter)
    assert status == 200
    assert len(result['pets']) > 0
    assert responce_headers['content-type'] == 'application/json' or 'application/xml'
    return status, result, get_key, filter, responce_headers



