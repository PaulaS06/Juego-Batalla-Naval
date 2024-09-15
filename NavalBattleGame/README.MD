## ¿Quién hizo esto?

Daniel Calle
Dilan Urrego

## ¿Qué es y para qué es?

- El juego de Batalla Naval es un juego de estrategia en el que el objetivo es hundir los barcos del oponente (en este caso la máquina) adivinando sus ubicaciones en un tablero.
- El juego de Batalla Naval en modalidad individual proporciona un desafío de lógica y estrategia, ya que el jugador debe deducir la posición de los barcos enemigos basándose en los resultados de sus disparos. Además, es entretenido y puede mejorar la capacidad de razonamiento lógico y la toma de decisiones del jugador.

## ¿Cómo lo hago funcionar?

- Prerrequisitos:
Instalar Python: Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo e instalarlo desde python.org.

Librerías: La única librería usada para este desarrollo es "random" que está incluida por defecto en pyhon, así que no debes descargar ninguna librería.

Código del Juego: Asegúrate de tener todos los archivos necesarios del proyecto en una carpeta organizada.

- Ejecución:
Navega a la carpeta: Una vez que hayas clonado el archivo, abre el cmd y navega a la carpeta en la que guardaste el archivo, por ejemplo:
C:\Users\durre\Documentos\Universidad\Semestre 4\Codigo Limpio\NavalBattleGame

Ejecuta el script main:
pyhon src\Console\NavalBattleConsole.py

Instrucciones en Pantalla: Una vez ejecutado, sigue las instrucciones que aparecerán en la consola para jugar. El juego interactuará contigo a través de mensajes de texto y comandos de teclado.
-
## ¿Cómo está hecho?

- Arquitectura del Proyecto:
Clases y Excepciones Personalizadas:

El proyecto define varias excepciones personalizadas para manejar errores específicos relacionados con la configuración y ejecución del juego, como NotEnoughSpace, BoardIsTooSmall, BoardIsTooBig, InvalidCoordinate, entre otras.

Clase Principal - NavalBattle:
Esta es la clase principal que gestiona toda la lógica del juego.

Ejecución Principal:
En el bloque if __name__ == "__main__":, el programa interactúa con el usuario para configurar el tamaño del tablero y la cantidad de barcos, y luego permite al jugador realizar disparos hasta que todos los barcos enemigos sean hundidos.

Bibliotecas Usadas:
random: Se utiliza para generar posiciones aleatorias para los barcos en el tablero.
Dependencias de Otros Proyectos:
No hay dependencias externas de otros proyectos o librerías adicionales más allá de las excepciones personalizadas y la biblioteca estándar random. Todo el juego está contenido dentro de una única clase y conjunto de excepciones personalizadas definidas en el mismo script.

- Organización de los Módulos:
Carpeta Principal: "NAVAL BATTLE GAME"

Contiene archivos y carpetas esenciales para el proyecto.
Archivos:
.gitignore: Define qué archivos o carpetas deben ser ignorados por el sistema de control de versiones (Git).
LICENSE: Contiene la licencia del proyecto, especificando los términos de uso, distribución y contribución.

Archivos:
settings.json: Configuraciones específicas para el entorno de desarrollo Visual Studio Code, como preferencias de formateo, extensiones recomendadas, etc.

__init__.py: Permite que la carpeta se trate como un paquete Python, facilitando la importación de módulos internos.
__pycache__: Carpeta generada automáticamente por Python para almacenar archivos compilados en bytecode (.pyc), lo que mejora la velocidad de carga de los módulos.


## Estructura sugerida

- Carpeta src:
Carpeta "src"
Esta carpeta contiene el código fuente del proyecto, dividido en módulos organizados.
Subcarpetas:
"Console"
Contiene la lógica del juego interactuando con la consola.
"NavalBattle"
Archivos:
NavalBattle.py: Contiene la implementación principal del juego de Batalla Naval, incluyendo clases y lógica relacionadas con la gestión del tablero, la colocación de barcos, y las mecánicas del juego.


- Carpeta tests: Pruebas Unitarias 
Carpeta "tests"
Contiene los archivos relacionados con las pruebas del proyecto, asegurando que las funcionalidades implementadas se comporten como se espera.
Archivos:
NavalBattleTests.py: Contiene los casos de prueba para la clase NavalBattle y sus métodos, probablemente utilizando un framework de pruebas como unittest o pytest.

## Uso

Para ejecutar las pruebas unitarias, desde la carpeta src, use el comando

`
  NAVAL BATTLE GAME\src> python -m unittest discover ..\tests -p '*test*.py'
`
Para poder ejecutarlas desde la carpeta raiz, debe indicar la ruta de busqueda donde se encuentran los
módulos, incluyendo las siguientes lineas al inicio del módulo de pruebas

`
  import sys
  sys.path.append("src")
`