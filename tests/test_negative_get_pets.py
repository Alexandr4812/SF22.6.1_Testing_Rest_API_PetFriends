from app import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import pytest
from settings import log_api, generate_string, russian_chars, chinese_chars, special_chars

pf = PetFriends()

#                     ТЕСТЫ ЗАПРОСОВ О ПИТОМЦАХ С НЕГАТИВНЫМ СЦЕНАРИЕМ
###########################################################################################

@pytest.mark.parametrize("filter",
                        [
                            generate_string(255)
                            , generate_string(1001)
                            , russian_chars()
                            , russian_chars().upper()
                            , chinese_chars()
                            , special_chars()
                            , 123
                        ],
                        ids =
                        [
                            '255 symbols'
                            , 'more than 1000 symbols'
                            , 'russian'
                            , 'RUSSIAN'
                            , 'chinese'
                            , 'specials'
                            , 'digit'
                        ])
@log_api
@pytest.mark.api
@pytest.mark.event
def test_get_all_pets_with_negative_filter(get_key, filter):
    '''Тест с использованием негативных параметров фильтра для проверки что статус запроса 400 а не 500'''
    status, result = pf.get_list_of_pets(get_key, filter)
    print(get_key, filter, status)
    assert status == 400
    return status, result, get_key, filter