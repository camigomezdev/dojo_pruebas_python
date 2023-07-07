"""
Codebreaker Class
"""
import random


class Codebreaker:
    def __init__(self) -> None:
        self.hidden_number = None

    def _get_random_number(self):
        return ''.join(random.sample("0123456789", 4))

    def set_hidden_number(self, hidden_numer=None):
        """
        Esta funcion debe guardar en self el numero especificado en 
        hidden_numer si no se pasa ningun numero debe generar
        un numero aleatorio
        """
        if hidden_numer is None:
            hidden_numer = self._get_random_number()

        try:
            self.is_valid_len_number(hidden_numer)
            self.is_a_number(hidden_numer)
            self.does_not_contain_repeated_digits(hidden_numer)
        except Exception as e:
            raise e

        self.hidden_number = hidden_numer

    def play(self):
        attempt = 1

        print('Vamos a Jugar Codebreaker!')
        print('Intenta adivinar el número oculto!')

        while True:
            print(f'Intento número {attempt}: ')
            number = input('')
            response = self.guess_number(number)
            print(f'Respuesta: {response}')

            if response == 'XXXX':
                print(f'¡Felicitaciones! Has ganado en {attempt} intentos')
                return attempt

            attempt += 1

    def guess_number(self, number=None):
        guess_position = ''
        guess_digit = ''

        for (index, digit) in enumerate(number):
            if digit == self.hidden_number[index]:
                guess_position += 'X'
            elif digit in self.hidden_number:
                guess_digit += '_'

        return guess_position + guess_digit

    def is_valid_len_number(self, number):
        if len(number) != 4:
            raise Exception('El numero debe tener 4 cifras')

        return True

    def is_a_number(self, number):
        if not number.isdecimal():
            raise Exception('Debes introducir un número entero de 4 cifras')

        return True

    def does_not_contain_repeated_digits(self, number):
        for digit in number:
            if number.count(digit) > 1:
                raise Exception('El número no puede contener dígitos \
repetidos')
        return True
