import pytest

from ..models import Poem, Poet


class TestPoet:
    @pytest.mark.django_db
    def test_str_only_first_name(self):
        fname = 'Нео'

        poet = Poet.objects.create(
            first_name=fname
        )

        assert str(poet) == f'Поэт(эсса): {fname}'

    @pytest.mark.django_db
    def test_str_with_full_name(self):
        fname = 'Нео'
        lname = 'Андерсен'

        poet = Poet.objects.create(
            first_name=fname,
            last_name=lname
        )

        assert str(poet) == f'Поэт(эсса): {fname} {lname}'


class TestPoem:
    @pytest.mark.django_db
    def test_str(self):
        title = 'Гуляка'
        fname = 'Сергей'
        lname = 'Есенин'
        poet = Poet.objects.create(
            first_name=fname, last_name=lname
        )

        poem = Poem.objects.create(
            author=poet,
            title=title,
            text='Я обманывать себя не стану'
        )

        assert str(poem) == f'{fname} {lname}: {title}'
