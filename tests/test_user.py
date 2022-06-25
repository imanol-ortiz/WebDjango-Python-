import pytest
from users.forms import Sign_upform

@pytest.mark.django_db
def test_user_creation():
    form = Sign_upform({
        'username' : 'pepe',
        'email' : 'pepe@gmail.com',
        'password1' : 'user123456',
        'password2' : 'user123456',
        
        })
    assert form.is_valid()