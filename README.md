# Dojo de Pruebas con Python

## Juego Codebreaker

1. El objetivo del juego es adivinar una secuencia numérica de 4 cifras oculta por el oponente en el menor número de intentos posibles.
2. La secuencia numérica puede consistir en números del 0 al 9, y no se repiten los números dentro de la secuencia.
3. Cada vez que hagas un intento, recibirás una retroalimentación en forma de "X" y "_".
   1. Una "X" significa que has adivinado correctamente un número en la posición correcta dentro de la secuencia.
   2. Un "_" significa que has adivinado correctamente un número, pero en una posición incorrecta dentro de la secuencia.
4. Utilizando esta retroalimentación, deberás deducir la secuencia correcta.
5. Con base en la retroalimentación recibida, realiza nuevos intentos ajustando tus suposiciones hasta que logres adivinar la secuencia correcta.
6. Continúa haciendo intentos y recibiendo retroalimentación hasta que logres descifrar la secuencia completa.

### Ejemplo:

**Intento número 1:** 1234
Retroalimentación: `__` (Dos guiones bajos)
Entre los número 1234 existen 2 que van en la secuencia final aunque aun no sabemos cuales son.

**Intento número 2:** 7890
Retroalimentación: `X_` (Una X y 1 guión bajo)
Entre los números 7890 existe 1 número que está en la posición correcta y 1 número que está en la secuencia, esto nos permite descartar los números 5 y 6 ya que los 4 números estan entre las secuencias del intento 1 y 2.

**Intento número 3:** 3170
Retroalimentación: `` (Un String vacío)
Entre los números 3170 no existe ningún número de la secuencia final, lo que nos dice que podemos descartar estos 4 números y la secuencia final está entre los número 2, 4, 8 y 9.

**Intento número 4:** 2498
Retroalimentación: `XX__` (2 Xs y 2 guiones bajos)
Existen dos números en la secuencia que están en la posición correcta y 2 que aún hay que corregir de pocisión.

**Intento número 5:** 8492
Retroalimentación: `XXXX` (4 Xs)
Hemos encontrado el número a adivinar en 5 intentos.

Recuerda que el desafío es encontrar la secuencia correcta en el menor número de intentos posible. ¡Buena suerte y disfruta jugando Codebreaker!

## Instalación:

```bash
python -m venv venv

# Activación en Unix
source venv/bin/activate

# Activación en Windows
venv\Scripts\activate

pip install -r requirements.txt
```

### Correr las pruebas:

pytest
``` bash
pytest -v
```

Coverage:

``` bash
coverage run --omit='tests/*' -m pytest
coverage report
coverage html
```
