# 🐢 Mini Turtle OO

Este proyecto es la **versión orientada a objetos** del ejercicio Mini-Turtle.  
Se implementa una clase `Tortuga` que permite simular movimientos básicos en consola
con independencia entre múltiples objetos.

---

## 📦 Estructura del Proyecto

mini_turtle_oo/
│
├── init.py
└── turtle_class.py
main.py
pyproject.toml
README.md


---

## 🧩 Clase Tortuga

La clase cumple con:

- Programación Orientada a Objetos
- Encapsulamiento (`self.posicion_x`)
- Sin variables globales
- Permite crear múltiples tortugas totalmente independientes

---

## 🐍 Ejemplo de Uso (main.py)

```python
from mini_turtle_oo import Tortuga

print("PRUEBA CON DOS TORTUGAS\n")

t1 = Tortuga()
t2 = Tortuga()

print("Tortuga 1 dibuja:\n")
t1.adelante(4)
t1.abajo(3)
t1.adelante(4)
t1.abajo(3)

print("\nTortuga 2 dibuja de forma independiente:\n")
t2.adelante(2)
t2.abajo(2)
t2.adelante(2)
t2.abajo(2)

print("\nComprobación de independencia:")
print("t1.posicion_x =", t1.posicion_x)
print("t2.posicion_x =", t2.posicion_x)

