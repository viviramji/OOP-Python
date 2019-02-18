<<<<<<< HEAD
# Taller OOP 1 Patrones de Diseño UTB

Vídeo juego libre con programación orientada a objetos.

## Angry Bird Nerd Version.

Una serie de jugadores tratará de dar en el blanco a un grupo de bad pigges 
que están a una distancia X ± 20 metros ingresando la velocidad inicial con la que se lanza un Angry Bird en tiro parabólico con una inclinación de 15°.

Cada jugador tendrá 3 intentos, si acierta al primero obtiene 10 puntos, si acierta al segundo obtiene 5, si acierta al tercero obtiene 2 puntos y por ultimo si no acierta tendrá 0 puntos, esto se hace durante 3 rondas y luego se muestra la tabla con los mejores jugadores.

>
```
t
```
=======
# Taller OOP 1 Patrones de Diseño UTB

Vídeo juego libre con programación orientada a objetos.

## Angry Bird Nerd Version.

Una serie de jugadores tratará de dar en el blanco a un grupo de * bad pigges *
que están a una distancia X ± 20 metros ingresando la velocidad inicial con la que se lanza un Angry Bird en tiro parabólico con una inclinación de 15°.

Cada jugador tendrá 3 intentos, si acierta al primero obtiene 10 puntos, si acierta al segundo obtiene 5, si acierta al tercero obtiene 2 puntos y por ultimo si no acierta tendrá 0 puntos, esto se hace durante 3 rondas y luego se muestra la tabla con los mejores jugadores.

## Contexto del Caso
> **Movimiento parabólico**
> *Es el realizado por un objeto cuya trayectoria describe una parábola. Se
> corresponde con la trayectoria ideal de un proyectil que se mueve en un medio que
> no ofrece resistencia al avance y que está sujeto a un campo gravitatorio uniforme.
> Tomado de Wikipedia.*

![Describiendo el sistema físico mediante el siguiente esquema](https://files.readme.io/63596dd-Captura.PNG)

Para realizar el proceso es necesaria una ecuación que calcula la distancia máxima en el plano x alcanzada por el Angry Bird ( proyectil ) o como se ve en la gráfica R, por lo general la gravedad se define como 9.8 m/s 2 , quedando la ecuación así:

![ecuacion](https://files.readme.io/069bbff-Captura.PNG)

## Codigo (solo la estructura de OOP)

```
class Player():
  def __init__(self, _name=None, _points=0.0):
    self.name = _name
    self.points = 0.0 if _points < 0.0 else _points

  #Returns true if player hit the mark or false otherwise 
  def throw(self, _speed, _min, _max):
    r = pow(_speed,2)*sin(math.radians(2*45))/9.8
    if( _min < r < _max):
      return True
    else:
      return False
     
  # set methods
  def setName(self, _name):
    self.name = _name
  def setPoint(self, _points):
    self.points = self.points +  _points

  # get methods
  def getName(self):
    return self.name
  def getPoints(self):
    return self.points

```


## Contribuciones

Este trabajo se basa en el caso estudio Aplicación del movimiento parabólico - Angry Birds.

Ficha técnica
Facultad de Ingeniería.
Programa de Ingeniería de Sistemas.
Algoritmos.
2014.
CASO 4-1.

>>>>>>> 69b8c0e71a2a065eb00041ea82e9b9e3f9e1ab1d
