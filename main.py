import os
from codebreaker import Codebreaker


def clean():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')

    # For macOS and Linux
    else:
        _ = os.system('clear')


if __name__ == '__main__':
    codebreaker = Codebreaker()
    action = input('Que deséa hacer? (1) Jugar, (2) Salir: ')

    while action == '1':
        print('Juagdor 1')
        hidden_number = input('Escriba el número oculto: ')
        codebreaker.set_hidden_number(hidden_number)
        clean()
        print('Juagdor 2')
        attempt_player_2 = codebreaker.play()

        print('--------------------')
        print('Juagdor 2')
        hidden_number = input('Escriba el número oculto: ')
        codebreaker.set_hidden_number(hidden_number)
        clean()
        print('Juagdor 1')
        attempt_player_1 = codebreaker.play()

        print('--------------------')
        if attempt_player_1 > attempt_player_2:
            print('El jugador 1 es el ganador')
        elif attempt_player_1 < attempt_player_2:
            print('El jugador 2 es el ganador')
        else:
            print('Wow! Es un empate!')
        
        print('--------------------')
        action = input('Que deséa hacer? (1) Jugar de nuevo, (2) Salir: ')
