# Keylogger

Este proyecto es un keylogger simple que registra las teclas pulsadas y las guarda en un archivo de texto con marcas de tiempo.

## Requisitos

- Python 3.x
- Biblioteca `pynput`

## Instalación

1. Clona este repositorio o descarga el archivo `keylogger.py`.
2. Instala la biblioteca `pynput` si no la tienes instalada:
    ```sh
    pip install pynput
    ```

## Uso

1. Ejecuta el script `keylogger.py`:
    ```sh
    python keylogger.py
    ```
2. El keylogger comenzará a registrar las teclas pulsadas y las guardará en un archivo llamado `keylog.txt` en la carpeta `Documentos` del usuario actual.

## Funcionamiento

- Cada vez que se presiona una tecla, se agrega al buffer.
- Al presionar `Enter`, el contenido del buffer se guarda en el archivo `keylog.txt` con una marca de tiempo.
- Al presionar `Espacio`, se agrega un espacio al buffer.
- Al presionar `Backspace`, se elimina el último carácter del buffer.
- Al presionar `Ctrl + L`, el contenido del buffer se guarda en el archivo `keylog.txt` con una marca de tiempo y el keylogger se detiene.

## Advertencia

Este script debe ser utilizado únicamente con fines educativos y en sistemas donde tengas permiso para registrar las teclas pulsadas. El uso no autorizado de un keylogger puede ser ilegal y violar la privacidad de las personas.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.
