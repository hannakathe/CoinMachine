![image](https://github.com/user-attachments/assets/f6148103-c90e-4d33-b1af-90711e9c4935)

# CoinMachine

# Proyecto de Máquina Tragamonedas con ESP32

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
  - Motores DC (3 unidades para los rodillos)
  - Servo motor (2 para las palancas liberadoras)
  - Buzzer
  - Sensores (para la combinación ganadora)
  - Botones (para la detección de palanca)
  - Estructura mecánica para la máquina tragamonedas
  - Fuente de alimentación adecuada

- **Software**
  - MicroPython para el ESP32
  - Biblioteca de control de motores (si es necesario)

## Estructura del Proyecto

Proyecto-Tragamonedas/ │ 

├── main.py # Código principal en MicroPython 

├── README.md # Documentación del proyecto 

├── hardware/ # Esquemas de conexiones y diseño de hardware 

├── software/ # Código y bibliotecas utilizadas └── docs/ # Documentación adicional


## Instalación y Configuración

1. **Conexiones de Hardware**
   - Conectar los motores DC a los pines del ESP32.
   - Conectar el servo motor para las palancas liberadoras.
   - Conectar el buzzer al ESP32.
   - Configurar los sensores para la detección de combinaciones ganadoras.
   - Configurar los botones para la palanca y correspondiente iniciación del juego

2. **Instalación de MicroPython**
   - Descargar e instalar MicroPython en el ESP32 siguiendo las [instrucciones oficiales](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html).

3. **Cargar el Código**
   - Subir el archivo `main.py` al ESP32 utilizando VS code.

## Uso

1. Acciona la palanca para iniciar el juego.
2. Los rodillos girarán y se detendrán en una combinación.
3. Si la combinación es ganadora, se activará el buzzer y se liberarán monedas.

## Funcionamiento

- **Inicio del Juego**: Al accionar la palanca, en la parte superior se presiona el boton que hace que se inicien los motores DC que hacen girar los rodillos.
- **Detección de Combinaciones Ganadoras**: Se implementa una lógica que verifica si los rodillos se detienen en una combinación ganadora.
- **Liberación de Monedas**: Se utiliza un servo motor o un mecanismo alternativo para liberar monedas cuando el jugador gana.

## Contribuciones

Para colaborar en el proyecto:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

