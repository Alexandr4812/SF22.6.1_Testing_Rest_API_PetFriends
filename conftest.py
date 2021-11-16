import pytest
from app import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password

@pytest.fixture()
def get_key():
    pf = PetFriends()
    status, key, _ = pf.get_app_key(valid_email, valid_password)
    assert status == 200
    assert 'key' in key
    return key




