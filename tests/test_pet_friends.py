# from app import PetFriends
# from settings import valid_email, valid_password, invalid_email, invalid_password
# import os
# import pytest
# from settings import log_api, generate_string, russian_chars, chinese_chars, special_chars, is_age_valid
#
# pf = PetFriends()
# ###
###########################################################################################
#@pytest.mark.parametrize("filter", ['', 'my_pets'], ids= ['empty string', 'only my pets'])
#@log_api
#@pytest.mark.api
#@pytest.mark.event
#def test_get_all_pets_with_valid_key(get_key, filter):
#    '''Проверяем что код статуса запроса 200 и список (всех питомцев) или (моих питомцев) не пустой
#    с использованием фикстуры и позитивных параметров фильтра.'''
#    status, result = pf.get_list_of_pets(get_key, filter)
#    assert status == 200
#    assert len(result['pets']) > 0
#    return status, result, get_key, filter
#
############################################################################################
#
#@pytest.mark.parametrize("filter",
#                       [
 #                           generate_string(255)
  #                          , generate_string(1001)
 #                           , russian_chars()
  #                          , russian_chars().upper()
  #                          , chinese_chars()
  #                          , special_chars()
  #                          , 123
  #                      ],
 #                       ids =
 #                       [
 #                           '255 symbols'
 #                           , 'more than 1000 symbols'
 #                           , 'russian'
 #                           , 'RUSSIAN'
 #                           , 'chinese'
 #                           , 'specials'
 #                           , 'digit'
 #                       ])
#@log_api
#def test_get_all_pets_with_negative_filter(get_key, filter):
#    '''Тест с использованием негативных параметров фильтра для проверки что статус запроса 400 а не 500'''
#    status, result = pf.get_list_of_pets(get_key, filter)
#    print(get_key, filter, status)
#    assert status == 400
#    return status, result, get_key, filter

#########################################################################################

#@log_api
#@pytest.mark.ui
#@pytest.mark.auth
#def test_get_api_key_valid_user(email=valid_email, password=valid_password):
#    '''Проверяем что код статуса запроса 200 и в переменной result
#    содержится слово key'''
#    status, result = pf.get_app_key(email, password)
 #   assert status == 200
 #   assert 'key' in result
 #   return status, result, email, password

##########################################################################################

# @log_api
# @pytest.mark.ui
# @pytest.mark.event
# def test_add_pets_with_valid_data(get_key,name='Fedor', animal_type='cat', age='3', pet_photo='images/Fedor.jpg'):
#     '''Проверяем что код статуса запроса 200 и что список с добавленными данными не пустой для этого
#     в переменную pet_photo сохраняем путь к файлу фотографии питомца, сохраняем ключ в переменную api_key,
#     проверяем статус ответа и что в ответе содержатся добавленные данные.
#     + используется фикстура для получения key
#      '''
#     pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#
#     #_, api_key = pf.get_app_key(valid_email, valid_password)
#     status, result = pf.add_new_pets(get_key, name, animal_type, age, pet_photo)
#     #assert status == 200
#     assert result['name'] == name
#     return status, result, get_key, name, animal_type, age, pet_photo

#############################################################################################

# @pytest.mark.ui
# @pytest.mark.event
# def test_delete_pet(get_key):
#     '''Проверяем возможность удаления питомца
#     + используется фикстура для получения key'''
#     #_, api_key = pf.get_app_key(valid_email, valid_password)
#     _, my_pets = pf.get_list_of_pets(get_key, 'my_pets')
#
#     if len(my_pets['pets']) == 0:
#         pf.add_new_pets(get_key, 'Murzik', 'cat', '5', 'images/Fedor.jpg')
#         _, my_pets = pf.get_list_of_pets(get_key, 'my_pets')
#
#     pet_id = my_pets['pets'][0]['id']
#
#     status, _ = pf.delete_pets(get_key, pet_id)
#     _, my_pets = pf.get_list_of_pets(get_key, 'my_pets')
#
#     #assert status == 200
#     assert pet_id not in my_pets.values()

###############################################################################################
#
# @pytest.mark.ui
# @pytest.mark.event
# def test_update_pet_info(get_key, name='из', animal_type='измененный', age='5'):
#     '''Проверяем возможность изменения данных питомца
#     + используется фикстура для получения key'''
#     #_, api_key = pf.get_app_key(valid_email, valid_password)
#     _, my_pets = pf.get_list_of_pets(get_key, 'my_pets')
#
#     if len(my_pets['pets']) > 0:
#         status, result = pf.update_pet_info(get_key, my_pets['pets'][0]['id'], name, animal_type, age)
#         #assert status == 200
#         assert result['name'] == name
#     else:
#         raise Exception("Питомцы отсутствуют")

# ################################################################################################
# @pytest.mark.parametrize("name", [
#    ''
#    , generate_string(255)
#    , generate_string(1001)
#    , russian_chars()
#    , russian_chars().upper()
#    , chinese_chars()
#    , special_chars()
#    , '123'
# ], ids=[
#    'empty'
#    , '255 symbols'
#    , 'more than 1000 symbols'
#    , 'russian'
#    , 'RUSSIAN'
#    , 'chinese'
#    , 'specials'
#    , 'digit'
# ])
# @pytest.mark.parametrize("animal_type", [
#    ''
#    , generate_string(255)
#    , generate_string(1001)
#    , russian_chars()
#    , russian_chars().upper()
#    , chinese_chars()
#    , special_chars()
#    , '123'
# ], ids=[
#    'empty'
#    , '255 symbols'
#    , 'more than 1000 symbols'
#    , 'russian'
#    , 'RUSSIAN'
#    , 'chinese'
#    , 'specials'
#    , 'digit'
# ])
# @pytest.mark.parametrize("age", [
#     ''
#     , '-1'
#     , '0'
#     , '1'
#     , '100'
#     , '1.5'
#     , '2147483647'
#     , '2147483648'
#     , special_chars()
#     , russian_chars()
#     , russian_chars().upper()
#     , chinese_chars()
# ], ids=[
#     'empty'
#     , 'negative'
#     , 'zero'
#     , 'min'
#     , 'greater than max'
#     , 'float'
#     , 'int_max'
#     , 'int_max + 1'
#     , 'specials'
#     , 'russian'
#     , 'RUSSIAN'
#     , 'chinese'])
# @pytest.mark.ui
# @pytest.mark.event
# def test_add_pets_with_valid_data_without_photo(get_key, name, animal_type, age):
#     '''Проверяем возможность добавления нового питомца без фото с различными данными
#     + используется фикстура для получения key'''
#     #_, api_key = pf.get_app_key(valid_email, valid_password)
#     status, result = pf.add_new_pet_without_photo(get_key, name, animal_type, age)
#     #assert status == 200
#     if name == '' or animal_type == '' or is_age_valid():
#         assert status == 400
#     else:
#         assert status == 200
#         assert result['name'] == name
#         assert result['age'] == age
#         assert result['animal_type'] == animal_type

###################################################################################################

# @pytest.mark.ui
# @pytest.mark.event
# def test_add_photo_at_pet(get_key, pet_photo='images/German.jpg'):
#     '''Проверяем возможность добавления новой фотографии питомца
#     + используется фикстура для получения key'''
#     pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#
#     #_, api_key = pf.get_app_key(valid_email, valid_password)
#     _, my_pets = pf.get_list_of_pets(get_key, 'my_pets')
#
#     if len(my_pets['pets']) > 0:
#         status, result = pf.add_photo_of_pet(get_key, my_pets['pets'][0]['id'], pet_photo)
#
#         _, my_pets = pf.get_list_of_pets(get_key, 'my_pets')
#
#         #assert status == 200
#         assert result['pet_photo'] == my_pets['pets'][0]['pet_photo']
#     else:
#         raise Exception("Питомцы отсутствуют")

###################################################################################################
#
# @pytest.mark.skip(reason="Баг в продукте - https://petfriends1.herokuapp.com/my_pets")
# @pytest.mark.ui
# @pytest.mark.event
# def test_add_pet_negative_age_number(get_key, name='Fedor', animal_type='cat', age='-3', pet_photo='images/Fedor.jpg'):
#     '''Проверка с негативным сценарием. Добавление питомца с отрицательным числом в переменной age.
#     Тест не будет пройден если питомец будет добавлен на сайт с отрицательным числом в поле возраст.
#      + используется фикстура для получения key'''
#     pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#
#     #_, api_key = pf.get_app_key(valid_email, valid_password)
#     _, result = pf.add_new_pets(get_key, name, animal_type, age, pet_photo)
#
#     assert age not in result['age'], 'Питомец добавлен на сайт с отрицательным числом в поле возраст'

#####################################################################################################
#
# @pytest.mark.api
# @pytest.mark.event
# def test_add_pet_with_four_digit_age_number(get_key, name='Fedor', animal_type='cat', age='1234', pet_photo='images/Fedor.jpg'):
#     '''Проверка с негативным сценарием. Добавление питомца с числом более трех знаков в переменной age.
#     Тест не будет пройден ели питомец будет добавлен на сайт с числом превышающим три знака в поле возраст.
#     + используется фикстура для получения key'''
#     pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#
#     #_, api_key = pf.get_app_key(valid_email, valid_password)
#     _, result = pf.add_new_pets(get_key, name, animal_type, age, pet_photo)
#     number = result['age']
#
#     assert len(number) < 4, 'Питомец добавлен на сайт с числом привышающим 3 знака в поле возраст'
#
# ######################################################################################################

#@pytest.mark.api
#@pytest.mark.event
#def test_add_pet_with_empty_value_in_variable_name(get_key, name='', animal_type='cat', age='2', pet_photo='images/Fedor.jpg'):
#    '''Проверяем возможность добавления питомца с пустым значением в переменной name
#    Тест не будет пройден если питомец будет добавлен на сайт с пустым значением в поле "имя"
#    + используется фикстура для получения key'''
#    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#
#    #_, api_key = pf.get_app_key(valid_email, valid_password)
 #   status, result = pf.add_new_pets(get_key, name, animal_type, age, pet_photo)
 #   #assert status == 200
 #   assert result['name'] != '', 'Питомец добавлен на сайт с пустым значением в имени'

#####################################################################################################
#
# @pytest.mark.api
# @pytest.mark.event
# def test_add_pet_with_a_lot_of_words_in_variable_name(get_key, animal_type='cat', age='2', pet_photo='images/Fedor.jpg'):
#     '''Проверка с негативным сценарием. Добавления питомца имя которого превышает 10 слов
#     Тест не будет пройден если питомец будет добавлен на сайт с именем состоящим из более 10 слов
#     + используется фикстура для получения key'''
#
#     name = 'Пабло Диего Хозе Франциско де Паула Хуан Непомукено Криспин Криспиано де ла Сантисима Тринидад Руиз и Пикассо'
#
#     _, api_key = pf.get_app_key(valid_email, valid_password)
#     status, result = pf.add_new_pets(get_key, name, animal_type, age, pet_photo)
#
#     list_name = result['name'].split()
#     word_count = len(list_name)
#
#    # assert status == 200
#     assert word_count < 10, 'Питомец добавлен с именем больше 10 слов'
#
# ####################################################################################################

# @pytest.mark.api
# @pytest.mark.event
# def test_add_pet_with_special_characters_in_variable_animal_type(get_key, name='Fedor', age='3', pet_photo='images/Fedor.jpg'):
#     '''Проверка с негативным сценарием. Добавление питомца с специальными символами вместо букв в переменной animal_type.
#     Тест не будет пройден если питомец будет добавлен на сайт с спец.символами вместо букв в поле порода.
#     + используется фикстура для получения key'''
#     animal_type = 'Cat%@'
#     symbols = '#$%^&*{}|?/><=+_~@'
#     symbol = []
#
#     pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#
#     #_, api_key = pf.get_app_key(valid_email, valid_password)
#     status, result = pf.add_new_pets(get_key, name, animal_type, age, pet_photo)
#
#     #assert status == 200
#     for i in symbols:
#         if i in result['animal_type']:
#             symbol.append(i)
#     assert symbol[0] not in result['animal_type'], 'Питомец добавлен с недопустимыми спец.символами'
#
# ######################################################################################################
#
# @pytest.mark.api
# @pytest.mark.event
# def test_add_pet_with_numbers_in_variable_animal_type(get_key, name='Fedor', animal_type='34562', age='3', pet_photo='images/Fedor.jpg'):
#     '''Проверка с негативным сценарием. Добавление питомца с цифрами вместо букв в переменной animal_type.
#     Тест не будет пройден если питомец будет добавлен на сайт с цифрами вместо букв в поле порода.
#     + используется фикстура для получения key'''
#     pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#
#     #_, api_key = pf.get_app_key(valid_email, valid_password)
#     status, result = pf.add_new_pets(get_key, name, animal_type, age, pet_photo)
#
#     #assert status == 200
#     assert animal_type not in result['animal_type'], 'Питомец добавлен на сайт с цифрами вместо букв в поле порода'

#######################################################################################################

# @pytest.mark.api
# @pytest.mark.event
# def test_add_pet_with_a_lot_of_words_in_variable_animal_type(get_key, name='Fedor', age='2', pet_photo='images/Fedor.jpg'):
#     '''Проверка с негативным сценарием. Добавления питомца название породы которого превышает 10 слов
#     Тест не будет пройден если питомец будет добавлен на сайт с названием породы состоящим из более 10 слов
#     + используется фикстура для получения key'''
#
#     animal_type = 'артезиано нормандский бассет гриффон миттельшнауцер ньюфаундленд аргентинский дог помесь с бриар басерон'
#
#     #_, api_key = pf.get_app_key(valid_email, valid_password)
#     status, result = pf.add_new_pets(get_key, name, animal_type, age, pet_photo)
#
#     list_animal_type = result['animal_type'].split()
#     word_count = len(list_animal_type)
#
#     #assert status == 200
#     assert word_count < 10, 'Питомец добавлен с названием породы больше 10 слов'

################################################################################################

##@pytest.mark.api
##@pytest.mark.auth
##def test_get_api_key_with_wrong_password_and_correct_mail(email=valid_email, password=invalid_password):
##    '''Проверяем запрос с невалидным паролем и с валидным емейлом.
##    Проверяем нет ли ключа в ответе'''
##    status, result = pf.get_app_key(email, password)
##    assert status == 403
 ##   assert 'key' not in result
##
#############################################################################################

#@pytest.mark.api
#@pytest.mark.auth
#def test_get_api_key_with_wrong_email_and_correct_password(email=invalid_email, password=valid_password):
#    '''Проверяем запрос с невалидным паролем и с валидным емейлом.
#    Проверяем нет ли ключа в ответе'''##
#    status, result = pf.get_app_key(email, password)
#    assert status == 403
 #   assert 'key' not in result
#
###################################################################################################

#def test_get_api_key_invalid_user(email=valid_email, password=valid_password):
#    '''Проверяем что код статуса запроса 200 и в переменной result
#    содержится слово key'''
#    status, result = pf.get_app_key_invalid_request(valid_email, valid_password)
#    print(status)#
#    print(result)





