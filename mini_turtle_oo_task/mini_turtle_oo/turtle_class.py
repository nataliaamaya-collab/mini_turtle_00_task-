class Tortuga:
    def __init__(self):
        self.posicion_x = 0

    def adelante(self, n):
        print(" " * self.posicion_x + "-" * n + ">")
        self.posicion_x += n

    def abajo(self, n):
        for _ in range(n - 1):
            print(" " * self.posicion_x + "|")
        print(" " * self.posicion_x + "v")

    def reiniciar(self):
        self.posicion_x = 0
