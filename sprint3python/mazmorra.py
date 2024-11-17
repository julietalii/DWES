from heroe import Heroe
from monstruo import Monstruo
from tesoro import Tesoro

class Mazmorra:
    def __init__(self, heroe):
        self.heroe = heroe
        self.monstruos = [Monstruo(f"Monstruo {i+1}") for i in range(3)]
        self.tesoro = Tesoro()

    def jugar(self):
        print("Héroe entra en la mazmorra.")
        for monstruo in self.monstruos:
            print(f"Te has encontrado con un {monstruo.nombre}.")
            self.enfrentar_enemigo(monstruo)
            if not self.heroe.esta_vivo():
                print("Héroe ha sido derrotado en la mazmorra.")
                return
            self.buscar_tesoro()
        
        print(f"¡{self.heroe.nombre} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")

    def enfrentar_enemigo(self, enemigo):
        while enemigo.esta_vivo() and self.heroe.esta_vivo():
            print("\n¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Defender")
            print("3. Curarse")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.heroe.atacar(enemigo)
                if enemigo.esta_vivo():
                    enemigo.atacar(self.heroe)
            elif opcion == "2":
                self.heroe.defenderse()
                enemigo.atacar(self.heroe)
                self.heroe.reset_defensa()
            elif opcion == "3":
                self.heroe.curarse()
                enemigo.atacar(self.heroe)
            else:
                print("Opción no válida.")

    def buscar_tesoro(self):
        print("Buscando tesoro...")
        self.tesoro.encontrar_tesoro(self.heroe)

