from app import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import pytest
from settings import log_api, generate_string, russian_chars, chinese_chars, special_chars

pf = PetFriends()

#                     ТЕСТЫ ЗАПРОСА API KEY С ПОЗИТИВНЫМ СЦЕНАРИЕМ
###########################################################################################

@log_api
@pytest.mark.ui
@pytest.mark.auth
def test_get_api_key_valid_user(email=valid_email, password=valid_password):
    '''Проверяем что код статуса запроса 200 и в переменной result
    содержится слово key.     • Заголовок ответа содержит:
    Обязательно - Content-type: aplication/json или application/xml'''
    status, result, responce_headers = pf.get_app_key(email, password)
    assert status == 200
    assert 'key' in result
    assert responce_headers['content-type'] == 'application/json' or 'application/xml'
    return status, result, email, password, responce_headers