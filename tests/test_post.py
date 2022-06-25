import pytest
from blogapp.forms import Postmodelform

@pytest.mark.django_db
def test_post_creation():
    form = Postmodelform({
        'titulo' : 'Hola',
        'contenido' : 'Texto ejemplo',
        
        })
    assert form.is_valid()