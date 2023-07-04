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
            print(f'Intento número {attempt}: ')
            number = input('')
            response = self.guess_number(number)
            print(f'Respuesta: {response}')

            if response == 'XXXX':
                print(f'¡Felicitaciones! Has ganado en {attempt} intentos')
                return attempt

            attempt += 1

    def guess_number(self, number=None):
        return 'XXXX'
