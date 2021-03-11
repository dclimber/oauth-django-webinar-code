import pytest

from ..models import Poet


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
