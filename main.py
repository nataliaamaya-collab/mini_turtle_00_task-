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
