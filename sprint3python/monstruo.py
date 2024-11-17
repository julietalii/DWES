class Monstruo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque = 8
        self.defensa = 3
        self.salud = 50

    def atacar(self, heroe):
        print(f"El monstruo {self.nombre} ataca a {heroe.nombre}.")
        dano = max(0, self.ataque - heroe.defensa)
        if dano > 0:
            heroe.salud -= dano
            print(f"El héroe {heroe.nombre} ha recibido {dano} puntos de daño.")
        else:
            print("El héroe ha bloqueado el ataque.")

    def esta_vivo(self):
        return self.salud > 0

