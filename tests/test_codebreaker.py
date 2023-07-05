"""
Unit test Codebreaker
"""
import pytest
from codebreaker import Codebreaker


@pytest.fixture
def codebreaker_instance():
     return Codebreaker()


def test_set_hidden_number_by_user(codebreaker_instance):
     codebreaker_instance.set_hidden_number('1234')

     assert codebreaker_instance.hidden_number == '1234'


def test_set_hidden_number_no_valid_len(codebreaker_instance):
     with pytest.raises(Exception) as e:
          codebreaker_instance.set_hidden_number('123')

     assert 'El numero debe tener 4 cifras' in str(e.value)


def test_set_random_number(mocker, codebreaker_instance):
     mocker.patch('codebreaker.Codebreaker._get_random_number',
                  return_value='1234')
     codebreaker_instance.set_hidden_number()

     assert codebreaker_instance.hidden_number == '1234'


def test_get_random_number(codebreaker_instance, mocker):
     mocker.patch('random.sample', return_value=['0', '9', '8', '7'])
     number = codebreaker_instance._get_random_number()
     assert number == '0987'


@pytest.mark.parametrize(
    "entry,expected",
    [
        ('0987', ''),
        ('3456', '__'),
        ('5634', 'XX'),
        ('1543', 'X__'),
        ('4321', '____'),
        ('1243', 'XX__'),
        ('1234', 'XXXX'),
    ]
)
def test_guess_number(codebreaker_instance, entry, expected):
     codebreaker_instance.set_hidden_number('1234')
     response = codebreaker_instance.guess_number(entry)

     assert response == expected

@pytest.mark.parametrize(
    "entry",
    [
        ('12345'),
        ('123'),
    ]
)
def test_is_valid_len_number_error(codebreaker_instance, entry):
     with pytest.raises(Exception) as e:
          codebreaker_instance.is_valid_len_number(entry)
     
     assert 'El numero debe tener 4 cifras' in str(e.value)


def test_is_valid_len_number(codebreaker_instance):
     result = codebreaker_instance.is_valid_len_number('1234')

     assert result
