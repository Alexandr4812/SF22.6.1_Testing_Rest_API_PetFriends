import functools

valid_email = 'forteslesson@gmail.com'
valid_password = 'qwerty'

invalid_email = 'forsson@gmail.com'
invalid_password = '12345'

##########################################################################################

def generate_string(n):
   return "x" * n

def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

# def is_age_valid(age):
#    # Проверяем, что возраст - это число от 1 до 49 и целое
#    return age.isdigit() \
#           and 0 < int(age) < 50 \
#           and float(age) == int(age)

#####################################################################################3

def log_api(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        signature = func(*args, **kwargs)
        status = str(signature[0])
        result = str(signature[1])
        request = str(signature[2:])
        with open('log.txt', 'w', encoding='utf8') as f:
            f.write(f'''Информация запроса:
------------------
Статус запроса:
{status}
Параметры запроса:
{request}

Информация ответа:
------------------
{result}''')
    return wrapper