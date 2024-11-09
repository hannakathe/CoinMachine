# CoinMachine.

## Proyecto de Máquina Tragamonedas con ESP32

## Descripción

Este proyecto consiste en la construcción de una máquina tragamonedas utilizando un ESP32, motores de corriente continua (DC), un buzzer y un sistema mecánico para la liberación de monedas. La máquina ofrece una experiencia de juego relativamente real, permitiendo a los usuarios jugar y ganar recompensas al obtener combinaciones ganadoras.

## Objetivos del Proyecto

- Crear una máquina tragamonedas funcional que simule el funcionamiento de una máquina de casino.
- Utilizar un ESP32 para controlar los motores DC que giran los rodillos.
- Implementar un sistema de detección de combinaciones ganadoras.
- Incorporar un buzzer para proporcionar retroalimentación sonora durante el juego.
- Desarrollar un mecanismo que libere monedas al detectar que un jugador ha ganado.
- Implementar todo lo aprendido durante la clase de arquitectura de hardware

## Componentes Requeridos

- **Hardware**
  - ESP32
  - L298N
  - Protoboard
  - Motores DC (3 unidades para los rodillos)
  - Servo motor (2 para las palancas liberadoras)
  - Buzzer (2)
  - Sensores (3 encode, para la combinación ganadora)
  - Botones (2 para la detección de palanca)
  - Balineras, resorte
  - Switch On/Off
  - Estructura mecánica para la máquina tragamonedas
  - Fuente de alimentación adecuada

- **Software**
  - MicroPython para el ESP32
  - Biblioteca de control de motores (si es necesario)

## Estructura del Proyecto

CoinMachine/ │

├── main.py                  # Archivo principal donde se importa todo

├── motor_control.py         # Controla la rotación de los motores (rodillos)

├── button_control.py         # Controlado mediante el movimiento de la palanca

├── buzzer_control.py        # Controla el buzzer

├── encoder_control.py        # Controla la ubicación inicial y final de los motores ademas controla el boton de frenado de los rodillos

├── prize_detection.py       # Lógica de detección de combinaciones ganadoras

├── coin_release.py          # Controla la liberación de monedas

├── README.md # Documentación del proyecto

## Instalación y Configuración

1. **Conexiones de Hardware**
   - Conectar los motores DC a los pines del ESP32.
   - Conectar los servo motorers a las palancas liberadoras, una en el primer almacen de monedas, y el otro en el almacen general del para liberación del premio.
   - Conectar el buzzer al ESP32.
   - Configurar los sensores para la detección de combinaciones ganadoras.
   - Configurar los botones para la palanca, boton superior para inicializacion del juego, y liberación de monedas del primer almacen, boton inferior para posible freno de los rodillos

2. **Instalación de MicroPython**
   - Descargar e instalar MicroPython en el ESP32 siguiendo las [instrucciones oficiales](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html).

3. **Cargar el Código**
   - Subir el archivo `main.py` al ESP32 utilizando VS code.

## Uso

1. Acciona la palanca para iniciar el juego.
2. Los rodillos girarán y se detendrán en una combinación.
3. Si la combinación es ganadora, se activará el buzzer y se liberarán monedas.

## Funcionamiento

- **Inicio del Juego**: Al accionar la palanca, en la parte superior se presiona el boton que hace que se inicien los motores DC que hacen girar los rodillos al mismo tiempo se le da la instrucción al servomotor de la plataforma liberadora del primer almacen de monedas liberando la moneda ingresando al almacen general donde estan las otras monedas.
- **Movimiento de los rodillos**: Al bajar la palanca y cuando vuelva a la ubicacion inicial se presionara el boton inferior realizando el frenado de los rodillos, y dandole un tiempo aleatoreo a cada rodillo para q siga rodando hasta q se detenga. Una vez los rodillos se detengan el encode analiza en que posición termino el rodillo.
- **Detección de Combinaciones Ganadoras**: Se implementa una lógica que verifica si los rodillos se detienen en una combinación ganadora, mediante el encode.
- **Liberación de Monedas**: Se utiliza un servo motor o un mecanismo alternativo para liberar monedas del almacen general cuando el jugador gana.

## Contribuciones

Para colaborar en el proyecto:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.
