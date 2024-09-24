## FLoreria "Ramo a tu medida"

class diana1071:
    id=0
    nombre=""
    tipo=""
    tamaño=0
    stock=0
    proveedor=""
    precio=0
    def mostrardatos(self):
        print("")
        print(f"Id: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Stock: {self.stock}")
        print(f"Provedor: {self.proveedor}")
        print(f"Precio: {self.precio}")
        print("")
    def listar_alumnos(self):
        print("")
        alumnos=["diana", "rodolfo", "najera", "azul", "andrea"]
        print("Alumnos: ")
        for x in alumnos:
            print(x)
    def tupla_profes(self):
        print("")
        profes=("nava", "meza", "roldan", "aldhair", "benavides")
        print("Profes: ")
        for x in profes:
            print(x)
    def diccionario_materia_califa(self):
        print("")
        print("Calificaciones")
        calificaciones={
            "ingles":10,
            "fisica":7,
            "calculo":7,
            "civica":6,
            "tutoria":8
        }
        for x,y in calificaciones.items():
            print(x,":",y)
    def altas(self):
        print("el registro se guardo satisfactoriamente")
    def bajas(self):
        print("el registro se elimino satisfactoriamente")
lilas=diana1071()
girasoles=diana1071()

lilas.id=1
lilas.nombre="lila"
lilas.tipo=" planta fanerógama"
lilas.tamaño=200
lilas.stock=250
lilas.proveedor="proflor"
lilas.precio=320

girasoles.id=2
girasoles.nombre="girasol"
girasoles.tipo="planta herbácea"
girasoles.tamaño=20
girasoles.stock=110
girasoles.proveedor="artiflora"
girasoles.precio=350

lilas.mostrardatos()
girasoles.mostrardatos()

lilas.listar_alumnos()
lilas.tupla_profes()
lilas.diccionario_materia_califa()
lilas.altas()
lilas.bajas()
