import pytest

from basics.forms import TagsAddForm


@pytest.mark.django_db
class TestTagForm:
    def test_form1(self):
        form = TagsAddForm({'name': None})
        is_valid = form.is_valid()
        assert is_valid == False

    def test_form_correct_data(self):
        form = TagsAddForm({'name': 'some tag'})
        is_valid = form.is_valid()
        assert is_valid == True
