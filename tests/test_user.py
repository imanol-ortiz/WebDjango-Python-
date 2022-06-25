import pytest
from django.contrib.auth.forms import UserCreationForm
from users.forms import Sign_upform

@pytest.mark.django_db
def test_user_creation():
    user = Sign_upform.objects.UserCreationForm(
        username = 'pepe',
        email = 'pepe@gmail.com',
        password1 = 'user123456',
        password2 = 'user123456',
    )
    assert user.username == 'pepe'