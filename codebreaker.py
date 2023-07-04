"""
Codebreaker Class
"""


class Codebreaker:
    def __init__(self) -> None:
        pass

    def set_hidden_number(self, hidden_numer=None):
        pass

    def play(self):
        attempt = 1

        print('Vamos a Jugar Codebreaker!')
        print('Intenta adivinar el número oculto!')

        while True:
            print(f'Intento número {attempt}:')
            number = input('')
            response = self.guess_number(number)
            print(f'Respuesta: {response}')

            attempt += 1

            if response == 'XXXX':
                print('¡Felicitaciones! Has ganado en {attempt} intentos')
                return attempt

    def guess_number(self, number=None):
        pass
