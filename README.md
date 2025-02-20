<h1 align="center">
Lab 1: Uso de OpenCV con Python (RA 1, RA 3 y RA 4) <br />
 </h1>
 <p align="center">
Alexander López-Parrado, PhD. <br />
Programación, I-2025 <br />
GDSPROC <br />
Uniquindío <br />
</p>

Esta práctica de laboratorio busca introducir el uso de la biblioteca OpenCV (*Open Computer Vision*) mediante el lenguaje de programación Python, OpenCV es una biblioteca para visión por computador y procesamiento de imágenes la cual será usada para el desarrollo del proyecto. En ese sentido, con esta práctica de laboratorio aprenderá aspectos básicos de procesamiento de imágenes con OpenCV usando Python, además se proponen algunos retos para poner en práctica sus habilidades en programación y a su vez construir código base para el desarrollo del proyecto.



## Instalación de OpenCV

Para instalar la biblioteca OpenCV solo digite el siguiente comando desde la línea de comandos: `python -m pip install opencv-contrib-python`. En todo caso, podrá encontrar una explicación detallada en el [siguiente video](https://www.youtube.com/watch?v=yYrWq3BfRuo). 

Si se genera algún error con pip solo tiene que actualizarlo, esta es la manera correcta de hacerlo desde línea de comandos: 
`python -m pip install --upgrade pip`
`pip install --upgrade pip`

Puede usar el programa de prueba [OpenCv.py](OpenCv.py) para verificar que la biblioteca OpenCV se ha instalado correctamente, ya que el programa imprime en la terminal la versión de OpenCV instalada.

ahora vamos a probar la cámara, para ello debes ejecutar el programa VerCamara.py con la siguiente instrucción:
python.exe VerCamara.py
El detalle lo encontrará en el siguiente enlace.


En esta sección repasará y pondrá en práctica de nuevo las sentencias condicionales del lenguaje de programación Python. Para lo anterior, considere el programa en el archivo [hrzones.py](hrzones.py) que realiza el cálculo de la frecuencia cardiaca máxima (*Heart Rate*) según la edad para una persona saludable [[1]](#1).

1. Ejecute el programa y realice pruebas con diferentes valores de edad.

2. Cree un nuevo programa (```hrzones2.py```) a partir de [hrzones.py](hrzones.py) que le solicite al usuario el valor de frecuencia cardiaca para un entrenamiento dado y le informe en qué zona de trabajo se realizó el entrenamiento (Z1, Z2, Z3, Z4 o Z5). Ayuda: Use la herramienta de Inteligencia Artificial (IA) Generativa ChatGPT para conocer sobre las zonas de trabajo, **no usarla para generar el código**.

3. Ahora use ChatGPT para generar el código del punto anterior, verifique el correcto funcionamiento del programa generado y compare con la implementación realizada por usted.

## Ciclos y Arreglos

En esta sección se considerarán las sentencias para ciclos y el uso de arreglos en el lenguaje de programación Python. Para esto, considere los programas de la sección anterior.

1. Cree un programa a partir de ```hrzones2.py``` que solicite al usuario un número de entrenamientos y que posteriormente solicite la frecuencia cardiaca promedio para cada una de ellos, calcular, almacenar e imprimir la zona de trabajo para cada uno de los entrenamientos.
2. Modifique el programa del punto 1 para que se calcule e imprima el porcentaje de entrenamientos que se encuentra en cada una de las zonas de trabajo (Z1, Z2, Z3, Z4 y Z5).
3. Ahora use ChatGPT para generar el código del punto anterior, verifique el correcto funcionamiento del programa generado y compare con la implementación realizada por usted.




## Funciones

Para terminar, en esta sección pondrá en práctica la creación de funciones en el lenguaje de programación Python. Recuerde que las funciones son construcciones que permiten crear código modular, escalable y de mayor legibilidad.

Para lo anterior, considere el programa que construyó en el punto 2 de la sección [Sentencias Condicionales](#sentencias-condicionales).

1. Realice una modificación al programa para que se le informe al usuario los valores promedio de frecuencia cardiaca para que el entrenamiento se realice en Z2. Para lo anterior, cree una función que realice el cálculo de la frecuencia cardiaca para lograr un entrenamiento en Z2 de acuerdo a la edad del usuario.

## Entrega del laboratorio

El laboratorio debe ser presentado mediante:

1. Repositorio en GitHub.
2. Informe de laboratorio.

El informe de laboratorio y el enlace al repositorio de GitHub deben ser compartidos en el enlace dispuesto para tal fin en la plataforma Google Classroom.

## Referencias

<a id="1">[1]</a> 
Mayo Clinic Staff, "Exercise intensity: How to measure it",url=https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/exercise-intensity/art-20046887.
