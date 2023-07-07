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
    assert '0987' == codebreaker_instance._get_random_number()


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
    assert expected == codebreaker_instance.guess_number(entry)


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
    assert codebreaker_instance.is_valid_len_number('1234')


@pytest.mark.parametrize(
    "entry",
    [
        "1234.0",
        "uno dos tres cuatro",
        "unodostrescuatro"
    ]
)
def test_is_a_number_error(codebreaker_instance, entry):
    with pytest.raises(Exception) as e:
        codebreaker_instance.is_a_number(entry)

    assert 'Debes introducir un número entero de 4 cifras' in str(e.value)


def test_is_a_number(codebreaker_instance):
    assert codebreaker_instance.is_a_number('1234')


@pytest.mark.parametrize(
    'entry',
    [
        '1123',
        '1233',
        '3345',
        '1112',
        '4444'
    ]
)
def test_does_not_contain_repeated_digits_error(codebreaker_instance, entry):
    with pytest.raises(Exception) as e:
        codebreaker_instance.does_not_contain_repeated_digits(entry)

    assert 'El número no puede contener dígitos repetidos' in str(e.value)


def test_does_not_contain_repeated_digits(codebreaker_instance):
    assert codebreaker_instance.does_not_contain_repeated_digits('5432')
