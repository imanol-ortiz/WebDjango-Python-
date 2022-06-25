import pytest
from blogapp.forms import commentform

@pytest.mark.django_db
def test_post_creation():
    form = commentform({
        'content' : 'Texto ejemplo',
        
        })
    assert form.is_valid()