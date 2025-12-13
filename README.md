# 🐢 Mini-Turtle OO

**– Versión Orientada a Objetos (POO)**

Este proyecto hace parte de la práctica **Evolución de Mini-Turtle** y corresponde al **Ejercicio 2**. En este ejercicio tomamos un programa sencillo y lo reorganizamos usando **Programación Orientada a Objetos (POO)**.eliminando el uso de variables globales y aplicando **encapsulamiento**.

La idea principal es aprender a usar **clases** y **objetos**, y a manejar la información (estado) de una forma más ordenada y clara.
eliminando el uso de variables globales y aplicando **encapsulamiento**.


## 🎯 Objetivo del Ejercicio

* Crear una **clase llamada `Tortuga`**.
* Guardar el estado de la tortuga (su posición) dentro de la clase.
* Inicializar la posición en `0` usando el método `__init__`.
* **No usar variables globales**.
* Poder crear **varias tortugas** que funcionen de manera independiente.
* Usar una **interfaz basada en objetos** en lugar de funciones sueltas.

---
## 🧠 Concepto Clave: Programación Orientada a Objetos

En lugar de usar funciones sueltas y variables globales, ahora:

* Usamos una **clase** como molde.
* Creamos **objetos** a partir de esa clase.
* Cada objeto tiene su propia información en memoria.

Esto se llama **encapsulamiento**: los datos y las acciones viven juntos dentro de la clase.

## 🧱 Estructura del Proyecto

```text
mini_turtle_oo_task
│
├── mini_turtle
│   ├── __init__.py      # Expone la clase Tortuga
│   └── turtle_class.py       # Contiene la definición de la clase Tortuga
│
├── main.py              # Archivo de prueba
├── pyproject.toml       # Configuración del proyecto
└── README.md            # Documentación
```

---
## 🐢 Clase Tortuga 


La clase Tortuga representa una tortuga que sabe moverse y dibujar. Cada tortuga tiene su propia posición, almacenada en un atributo.

Atributo

self.posicion_x: guarda la posición horizontal de la tortuga. Se inicia en 0.

Constructor

El método __init__ se ejecuta cuando se crea una tortuga nueva y sirve para inicializar su estado:

```python
def __init__(self):
self.posicion_x = 0
```

### Métodos

* `adelante(n)`: mueve la tortuga hacia adelante `n` pasos.
* `abajo(n)`: dibuja líneas hacia abajo sin cambiar la posición horizontal.
* `reiniciar()`: devuelve la posición a 0.

Toda la lógica se maneja usando `self`, sin variables globales.


## 📦 Interfaz del Paquete

El archivo __init__.py expone la clase Tortuga para que el usuario pueda importarla fácilmente:

```
from .turtle_class import Tortuga
```

## ▶️ Prueba del Programa (`main.py`)

En el archivo `main.py` se crean **dos objetos diferentes** para demostrar que cada uno mantiene su estado de forma independiente:


codigo del proyecto

```python
from mini_turtle_oo import Tortuga

print("PRUEBA CON DOS TORTUGAS\n")

t1 = Tortuga()
t2 = Tortuga()

# TORTUGA 1: dibuja una escalera de 2 escalones
print("Tortuga 1 dibuja:\n")
t1.adelante(5)
t1.abajo(5)
t1.adelante(5)
t1.abajo(5)

# TORTUGA 2: dibuja otra escalera independiente de 2 escalones
print("\nTortuga 2 dibuja de forma independiente:\n")
t2.adelante(4)
t2.abajo(3)
t2.adelante(4)
t2.abajo(3)

print("\nComprobación de independencia:")
print("t1.posicion_x =", t1.posicion_x)
print("t2.posicion_x =", t2.posicion_x)
```
<img width="542" height="593" alt="Captura de pantalla 2025-12-11 225027" src="https://github.com/user-attachments/assets/1e324bb1-1b97-450c-8aef-b0a09cc2bfc3" />

Al final, cada tortuga tiene su propia posición, lo que demuestra el encapsulamiento.

---

## ⚙️ Requisitos

* Python 3.8 o superior
* No se requieren librerías externas

---

## 🚀 Cómo Ejecutar

Desde la carpeta del proyecto:

```
python main.py
```



## 📚 Qué se Aprende con este proyecto

* Qué es una **clase** y un **objeto**
* Cómo usar el método `__init__`
* Qué es el **encapsulamiento**
* Por qué es mejor evitar variables globales
* Cómo crear programas más organizados





















