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
    def tsucursales(self):
        print("")
        sucursales=["zapata", "henequen", "curva", "torres", "aztecas"]
        print("Sucursales: ")
        for x in sucursales:
            print(x)
    def templeados(self):
        print("")
        empleados=("rodolfo", "najera", "diana", "azul", "andrea")
        print("Empleados: ")
        for x in empleados:
            print(x)
    def tinventario(self):
        print("")
        print("Inventario")
        inventario={
            "lilas":100,
            "girasoles":70,
            "tulipanes":70,
            "cactus":60,
            "margaritas":80
        }
        for x,y in inventario.items():
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

lilas.tsucursales()
lilas.templeados()
lilas.tinventario()
lilas.altas()
lilas.bajas()
