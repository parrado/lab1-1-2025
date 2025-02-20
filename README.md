<h1 align="center">
Lab 1: Uso de OpenCV con Python (RA 1, RA 3 y RA 4) <br />
 </h1>
 <p align="center">
Alexander López-Parrado, PhD. <br />
Programación, I-2025 <br />
GDSPROC <br />
Uniquindío <br />
</p>

Esta práctica de laboratorio busca introducir la biblioteca OpenCV (*Open Computer Vision*) y su uso mediante el lenguaje de programación Python, OpenCV es una biblioteca para visión por computador y procesamiento de imágenes la cual será usada para el desarrollo del proyecto [[1]](#1). En ese sentido, con esta práctica de laboratorio aprenderá aspectos básicos de procesamiento de imágenes con OpenCV usando Python, además se proponen algunos retos para poner en práctica sus habilidades en programación y a su vez construir código base para el desarrollo del proyecto.



## Instalación de OpenCV

Para instalar la biblioteca OpenCV solo digite el siguiente comando desde una terminal: `python -m pip install opencv-contrib-python`. En todo caso, podrá encontrar una explicación detallada en el [siguiente video](https://www.youtube.com/watch?v=yYrWq3BfRuo). 

Si se genera algún error con `pip` solo tiene que actualizarlo, esta es la manera correcta de hacerlo desde una terminal: 
`python -m pip install --upgrade pip`
`pip install --upgrade pip`

Puede usar el programa de prueba [OpenCv.py](OpenCv.py) para verificar que la biblioteca OpenCV se ha instalado correctamente, en particular el programa imprime en la terminal la versión de OpenCV instalada.

Finalmente, con el programa (VerCamara.py)[VerCamara.py] se verificará el acceso correcto a la cámara, al ejecutarse deberá abrir una ventana en donde se visualiza la cámara frontal de su computador portátil, también puede usarlo para acceder a una cámara conectada a alguno de los puertos USB. Analice el funcionamiento del programa (VerCamara.py)[VerCamara.py].


## Representación de imágenes en OpenCV






## Reto 1: Identificación de colores



Para lo anterior, considere el programa que construyó en el punto 2 de la sección [Sentencias Condicionales](#sentencias-condicionales).

## Reto 2: Operadores para detección de bordes




## Entrega del laboratorio

El laboratorio debe ser presentado mediante:

1. Repositorio en GitHub.
2. Informe de laboratorio.

El informe de laboratorio y el enlace al repositorio de GitHub deben ser compartidos en el enlace dispuesto para tal fin en la plataforma Google Classroom.

## Referencias

<a id="1">[1]</a> 
OpenCV team, About OpenCV",url=[https://opencv.org/](https://opencv.org/about/).
