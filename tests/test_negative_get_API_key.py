from app import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import pytest
from settings import log_api, generate_string, russian_chars, chinese_chars, special_chars

pf = PetFriends()

#                     ТЕСТЫ ЗАПРОСА API KEY С НЕГАТИВНЫМ СЦЕНАРИЕМ
###########################################################################################
@pytest.mark.parametrize("email", [
    '',
    valid_email,
    invalid_email
], ids=[
    'empty',
    'valid email',
    'invalid email'
])
@pytest.mark.parametrize("password", [
    '',
    invalid_password
], ids=[
    'empty',
    'invalid password'
])
@log_api
@pytest.mark.api
@pytest.mark.auth
def test_get_api_key_with_wrong_email_and_correct_password(email, password):
    '''Проверяем запрос с невалидным паролем и с валидным емейлом.
    Проверяем нет ли ключа в ответе'''
    status, result = pf.get_app_key(email, password)
    assert status == 403
    assert 'key' not in result
    return status, result, email, password